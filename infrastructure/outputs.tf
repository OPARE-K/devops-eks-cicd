output "cluster_name" {
  value = aws_eks_cluster.this.name
}

output "region" {
  value = var.region
}

output "ecr_repo" {
  value = aws_ecr_repository.app.repository_url
}

output "oidc_role_arn" {
  value = aws_iam_role.github_actions.arn
}
