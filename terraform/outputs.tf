output "cluster_name" {
  value = module.eks.cluster_name
}
output "region" {
  value = var.aws_region
}
output "vpc_id" {
  value = module.vpc.vpc_id
}
output "configure_kubectl" {
  value = "aws eks update-kubeconfig --region ${var.aws_region} --name ${module.eks.cluster_name}"
}
