variable "project" {
  description = "Project ID"
  default     = "splendid-planet-426504-t8"
}
variable "credentials" {
  description = "Service Account Credentials"
  default     = "./credentials/gcpSA1.json"
}


variable "bq_dataset_name" {
  description = "My BigQuery dataset name"
  default     = "demo_dataset"
}

variable "location" {
  description = "Project Location for the bucket"
  default     = "US"
}

variable "region" {
  description = "Project Location for the bucket"
  default     = "us-west1"
}


variable "gcs_bucket_name" {
  description = "My GCS bucket name"
  default     = "splendid-planet-bucket"
}

variable "gcs_storage_class" {
  description = "Storage class for the bucket"
  default     = "STANDARD"
}