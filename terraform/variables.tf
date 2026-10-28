variable "aws_region" {
  description = "AWS region for the sandbox cluster"
  type        = string
  default     = "ap-south-1"
}
variable "cluster_name" {
  description = "EKS cluster name"
  type        = string
  default     = "secure-platform-eks"
}
variable "kubernetes_version" {
  description = "Supported EKS Kubernetes version; verify availability in your region"
  type        = string
  default     = "1.31"
}
variable "node_instance_type" {
  description = "EC2 instance type for managed worker nodes"
  type        = string
  default     = "t3.medium"
}
variable "desired_size" {
  type    = number
  default = 2
}
variable "min_size" {
  type    = number
  default = 1
}
variable "max_size" {
  type    = number
  default = 3
}
