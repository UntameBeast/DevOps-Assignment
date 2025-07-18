terraform {
  backend "s3" {
    bucket = "terraform-statefile-githubflow"
    key    = "ecs/terraform.tfstate"
    region = "us-east-1"
  }
}
