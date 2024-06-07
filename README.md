# Dynamic DNS Updater for Cloudflare

When your budget is 0 and you can't find a truly free DDNS service, I got you covered. This repository contains scripts to dynamically update the DNS records for a domain managed by Cloudflare. It includes:

- A script to get the record ID for a specific DNS record.
- A script to update the DNS record with the current public IPv4 address.
- A `requirements.txt` file for the necessary Python packages.
- A `.env.example` file for environment variable configuration.

## Files

- `update_dns_record.py`: Script to update the DNS record with the current public IPv4 address.
- `list_dns_records.py`: Script to list DNS records and get the record ID.
- `requirements.txt`: List of required Python packages.
- `.env.example`: Example environment variable configuration file.

## Prerequisites

- Python 3.x
- Cloudflare account and API token

## Setup

1. Clone this repository:

   ```sh
   git clone https://github.com/Collert/open_ddns.git
   cd yourrepo
   ```

2. Create a virtual environment and activate it:

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:

   ```sh
   pip install -r requirements.txt
   ```

4. Copy the `.env.example` file to `.env` and fill in your details:

   ```sh
   cp .env.example .env
   ```

   Edit the `.env` file with your Cloudflare account details and DNS record information.

## Usage

### Getting the Record ID

To list DNS records and get the record ID:

1. Run the `list_dns_records.py` script:

   ```sh
   python list_dns_records.py
   ```

   This will output the DNS records along with their IDs. Note down the `record_id` for the DNS record you want to update.

### Updating the DNS Record

To update the DNS record with the current public IPv4 address:

1. Ensure the `.env` file contains the correct `record_id` obtained from the previous step.
2. Run the `update_dns_record.py` script:

   ```sh
   python update_dns_record.py
   ```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
