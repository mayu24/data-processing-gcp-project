# File: terraform/main.tf
provider "google" {
  project = "root-rock-413418"
  region  = "us-central1"
}

  resource "google_dataproc_cluster" "my-dataproc-cluster" {
  name             = "my-dataproc-cluster"
  region           = "us-central1"
  cluster_config {
    master_config {
      machine_type = "e2-medium" // Specify a machine type that meets the minimum requirements
      disk_config {
        boot_disk_size_gb = 50// Specify the boot disk size in GB
      }
    }
    worker_config {
      machine_type = "e2-medium" // Specify a machine type that meets the minimum requirements
      disk_config {
        boot_disk_size_gb = 50 // Specify the boot disk size in GB
      }
      num_instances = 2 // Specify the number of worker instances
    }
  }
}

