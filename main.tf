# File: terraform/main.tf
provider "google" {
  project = "root-rock-41341"
  region  = "us-central1"
}

  resource "google-dataproc-cluster" "my-dataproc-cluste" {
  name             = "my-dataproc-cluste"
  region           = "us-central1"
  project_id       = "root-rock-41341"
  cluster_config {
    master_config {
      machine_type = "n1-standard-4" // Specify a machine type that meets the minimum requirements
      disk_config {
        boot_disk_size_gb = 50// Specify the boot disk size in GB
      }
    }
    worker_config {
      machine_type = "n1-standard-4" // Specify a machine type that meets the minimum requirements
      disk_config {
        boot_disk_size_gb = 50 // Specify the boot disk size in GB
      }
      num_instances = 2 // Specify the number of worker instances
    }
  }
}

