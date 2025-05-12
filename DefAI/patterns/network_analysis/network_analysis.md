# Network Analysis Pattern

## Overview
This pattern analyzes network traffic for anomalies, including latency issues, DDoS, and inbound/outbound data analysis. 

Version: "1.0"

## Inputs
- File: `test_data.pcap`
- Latency Threshold: `0.1`
- Traffic Spike Threshold: `100`

## Example Input
`./network_data.pcap`

## Modules

#### 1. Inbound/Outbound Traffic Analysis
- **Inbound Traffic Analysis**: Identify suspicious traffic sources.
- **Outbound Traffic Analysis**: Monitor for potential data ex-filtration.
- **Latency Check**: Flag packets with high delays.

## Steps
1. Read the `.pcap` file using the `wireshark_capture` input.
2. Extract:
   - Packet sizes
   - Source and destination IPs
   - Protocol types
3. Compare traffic patterns to thresholds:
   - Latency: Alert if `latency_threshold` is exceeded.
   - DDoS: Check for traffic spikes beyond `traffic_spike_threshold`.
4. Generate:
   - Alerts for anomalies.
   - Summary report.

## Expected Outputs
- Alert: "Potential DDoS detected from IP 192.168.1.1"
- Summary: "90% of traffic is outbound to external IPs."