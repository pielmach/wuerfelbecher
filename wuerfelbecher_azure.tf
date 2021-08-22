terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 2.73"
    }
  }

  required_version = ">= 1.0.5"
}

provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "rg" {
  name     = "wuerfelbecher"
  location = "westeurope"
}

resource "azurerm_virtual_network" "vnet" {
  name                = "wuerfelbecher-vnet"
  address_space       = ["10.0.0.0/16"]
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
}

resource "azurerm_subnet" "snet" {
  name                 = "wuerfelbecher-snet"
  address_prefixes     = ["10.0.0.0/24"]
  resource_group_name  = azurerm_resource_group.rg.name
  virtual_network_name = azurerm_virtual_network.vnet.name

  delegation {
    name = "delegation"

    service_delegation {
      name    = "Microsoft.ContainerInstance/containerGroups"
      actions = ["Microsoft.Network/virtualNetworks/subnets/action"]
    }
  }
}

resource "azurerm_network_profile" "netp" {
  name                = "wuerfelbecher-netp"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name

  container_network_interface {
    name = "wuerfelbecher-nic"

    ip_configuration {
      name      = "wuerfelbecher-ipconfig"
      subnet_id = azurerm_subnet.snet.id
    }
  }
}

resource "azurerm_container_group" "cg" {
  name                = "wuerfelbecher-bot"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  os_type             = "linux"
  ip_address_type     = "private"
  network_profile_id  = azurerm_network_profile.netp.id
  restart_policy      = "Never"

  container {
    name                         = "wuerfelbecher-bot"
    image                        = "ghcr.io/pielmach/wuerfelbecher/wuerfelbecher:${var.wuerfelbecher_release}"
    cpu                          = "0.5"
    memory                       = "0.5"
    environment_variables        = {}
    secure_environment_variables = { "DISCORD_BOT_TOKEN" = var.discord_bot_token }

    ports {
      port     = 80
      protocol = "TCP"
    }
  }
}

variable "wuerfelbecher_release" {
  description = "Wuerfelbecher release to deploy from github container registry"
  type        = string
  default     = "v1.2.1"
}

variable "discord_bot_token" {
  description = "Secret access token for the discord bot"
  type        = string
}
