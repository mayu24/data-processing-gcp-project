def preprocess_data(data):
    # Perform data preprocessing tasks here
    # For example:
    preprocessed_data = data.strip().upper()  # Example: Stripping whitespace and converting to uppercase
    return preprocessed_data

def process_data(event, context):
    file_name = event['name']
    print(f"Processing file: {file_name}")

    # Read the file content from Cloud Storage
    file_blob = storage_client.bucket(my_bucket_dataproc).get_blob(file_name)
    file_content = file_blob.download_as_string().decode('utf-8')

    # Preprocess the data
    preprocessed_content = preprocess_data(file_content)

    # Perform further processing or store the preprocessed data
    # For example, you can write the preprocessed data to another Cloud Storage bucket
    preprocessed_blob = storage_client.bucket(my_bucket_dataproc_preprocess).blob(file_name)
    preprocessed_blob.upload_from_string(preprocessed_content, content_type='text/plain')

    print("Data preprocessing completed.")
