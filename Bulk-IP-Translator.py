import socket
import tkinter as tk

def ip_to_dns(ip_address):
    try:
        domain_name = socket.gethostbyaddr(ip_address)
        return domain_name[0]
    except socket.herror:
        return "No DNS entry found for the IP address."

def translate_ips():
    ip_addresses = text_input.get("1.0", "end-1c")
    translated_results.delete("1.0", tk.END)
    results = []
    for ip_address in ip_addresses.split('\n'):
        ip_address = ip_address.strip()
        if ip_address:
            dns_name = ip_to_dns(ip_address)
            results.append((ip_address, dns_name))
    for ip, dns_name in results:
        translated_results.insert(tk.END, f"IP: {ip}, DNS: {dns_name}\n")

# Create the main window
root = tk.Tk()
root.title("Bulk IP Translator")

# Create text input field for IP addresses
text_input = tk.Text(root, height=10, width=40)
text_input.grid(row=0, column=0, padx=10, pady=10)

# Create button to trigger translation
translate_button = tk.Button(root, text="Translate", command=translate_ips)
translate_button.grid(row=0, column=1, padx=10, pady=10)

# Create text output field for translated results
translated_results = tk.Text(root, height=10, width=40)
translated_results.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Run the GUI
root.mainloop()