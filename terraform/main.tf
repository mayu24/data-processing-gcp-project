# File: terraform/main.tf
provider "google" {
  project = "your-project-id"
  region  = "us-central1"
}

resource "google_dataproc_cluster" "example_cluster" {
  name           = "example-cluster"
  project        = "your-project-id"
  region         = "us-central1"
  cluster_config {
    master_config {
      num_instances = 1
      machine_type  = "n1-standard-4"
    }
    worker_config {
      num_instances = 2
      machine_type  = "n1-standard-4"
    }
  }
}

