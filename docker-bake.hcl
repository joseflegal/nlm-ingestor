
target "nlm-ingestor" {
  dockerfile = "Dockerfile"
  tags       = [for project in ["gnome2-uat", "gnome2-production", "gnome-chonk", "gnome2-infra"] : "australia-southeast1-docker.pkg.dev/${project}/images/nlm-parser:${BRANCH_NAME}"]
}

variable "BRANCH_NAME" {
  default = "fixed"
}


