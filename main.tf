# File: terraform/main.tf
provider "google" {
  project = "root-rock-41341"
  region  = "us-central1"
}

resource "google_dataproc_cluster" "my-dataproc-cluster" {
  name           = "my-dataproc-cluster"
  project        = "root-rock-413418"
  region         = "us-central1"
  cluster_config {
    master_config {
      num_instances = 1
      machine_type  = "n1-standard-4"
      disk_config {
        boot_disk_size_gb = 50 
      }
    }
    }
    worker_config {
      num_instances = 2
      machine_type  = "n1-standard-4"
      disk_config {
        boot_disk_size_gb = 50
      }

    }
  }
}
