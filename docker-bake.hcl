
target "default" {
  dockerfile = "Dockerfile"
  tags       = tags($BRANCH_NAME)
}

variable "BRANCH_NAME" {
  default = "test"
}
function "tags" {
  params = [branch_name]
  result = branch_name == "fixed" ? [for project in ["gnome2-uat", "gnome2-production", "gnome-chonk", "gnome2-infra"] : "australia-southeast1-docker.pkg.dev/${project}/images/nlm-parser:${BRANCH_NAME}"] : ["nlm-parser"]

}


