def calculate_bit_timing(clock_freq_mhz, target_baud_kbps):
    """
    Simple calculator for CAN bit timing segments.
    Note: Real-world calculation is more complex (sample point, SJW).
    """
    tq_per_bit = 16 # Target time quanta per bit (typical 8-25)
    
    clock_freq = clock_freq_mhz * 1_000_000
    target_baud = target_baud_kbps * 1000
    
    prescaler = clock_freq / (target_baud * tq_per_bit)
    
    print(f"--- CAN Bit Timing Calculator ---")
    print(f"Clock: {clock_freq_mhz} MHz")
    print(f"Target Baud: {target_baud_kbps} kbps")
    print(f"Target TQ/bit: {tq_per_bit}")
    print(f"Calculated Prescaler: {prescaler}")
    
    if not prescaler.is_integer():
        print("WARNING: Prescaler is not an integer. Adjust TQ or Clock.")
    else:
        # Typical 80% sample point
        tseg1 = int(tq_per_bit * 0.8) - 1 # Sync seg is 1 TQ
        tseg2 = tq_per_bit - 1 - tseg1
        
        print(f"\nConfiguration:")
        print(f"Prescaler: {int(prescaler)}")
        print(f"Sync Seg: 1")
        print(f"TSEG1 (Prop + Phase1): {tseg1}")
        print(f"TSEG2 (Phase2): {tseg2}")
        print(f"Sample Point: {(1 + tseg1) / tq_per_bit * 100:.1f}%")

if __name__ == "__main__":
    calculate_bit_timing(clock_freq_mhz=80, target_baud_kbps=500)
