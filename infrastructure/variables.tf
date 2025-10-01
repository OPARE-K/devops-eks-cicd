variable "region" {
  type    = string
  default = "eu-west-2"
}

variable "project_name" {
  type    = string
  default = "devops-eks-cicd"
}

variable "vpc_cidr" {
  type    = string
  default = "10.50.0.0/16"
}

variable "k8s_version" {
  type    = string
  default = "1.28"
}

variable "node_type" {
  type    = string
  default = "t3.medium"
}

variable "desired_nodes" {
  type    = number
  default = 2
}

variable "github_owner" {
  type    = string
  default = "OPARE-K" # change to your GitHub username/org
}

variable "github_repo" {
  type    = string
  default = "devops-eks-cicd" # change to your repo name
}
