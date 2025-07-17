terraform {
  backend "s3" {
    bucket = "your-terraform-state-bucket"
    key    = "ecs/terraform.tfstate"
    region = "us-east-1"
  }
}
