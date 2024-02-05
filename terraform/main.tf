# File: terraform/main.tf
provider "google" {
  project = "root-rock-41341"
  region  = "us-central1"
}

resource "google_dataproc_cluster" "my_dataproc_cluster" {
  name           = "my_dataproc_cluster"
  project        = "root-rock-41341"
  region         = "us-central1"
  cluster_config {
    master_config {
      num_instances = 1
      machine_type  = "e2-micro"
    }
    worker_config {
      num_instances = 2
      machine_type  = "e2-micro"
    }
  }
}
