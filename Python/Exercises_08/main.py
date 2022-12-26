from http.client import SWITCHING_PROTOCOLS
from Devices import Firewall
# Create a firewall instance
firewall27 = Firewall("firewall27")
# Configure it
firewall27.configure_firewall()
# Create a firewall instance
firewall28 = Firewall("firewall28")
# Verify a CRC
firewall28.calculate_crc("dummy data")



from Devices import Switch
# Create a Switch Config
Switch01 = Switch("Switch01")
# Configure it
Switch01 = SWITCHING_PROTOCOLS
# Create a Switch Config
Switch02 = Switch("Switch02")
# Verify protocol
Switch02.spanning-tree("dummy data")