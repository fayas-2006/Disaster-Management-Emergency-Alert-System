# Disaster Management & Emergency Alert System

print("===================================")
print(" DISASTER MANAGEMENT ALERT SYSTEM ")
print("===================================")

print("\nSelect a Disaster")
print("1. Flood")
print("2. Fire")
print("3. Earthquake")
print("4. Cyclone")

choice = int(input("\nEnter your choice (1-4): "))

print("\n----- SAFETY INSTRUCTIONS -----")

if choice == 1:
    print("Disaster: Flood")
    print("- Move to higher ground.")
    print("- Avoid walking in flood water.")
    print("- Keep emergency supplies ready.")
    print("- Follow government alerts.")

elif choice == 2:
    print("Disaster: Fire")
    print("- Stay calm.")
    print("- Use the nearest exit.")
    print("- Do not use elevators.")
    print("- Call the fire department.")

elif choice == 3:
    print("Disaster: Earthquake")
    print("- Drop, Cover and Hold.")
    print("- Stay away from windows.")
    print("- Move to an open area after shaking stops.")
    print("- Keep an emergency kit ready.")

elif choice == 4:
    print("Disaster: Cyclone")
    print("- Stay indoors.")
    print("- Close all windows and doors.")
    print("- Keep food, water and medicines ready.")
    print("- Listen to weather updates.")

else:
    print("Invalid Choice!")

print("\nEmergency Numbers")
print("Police   : 100")
print("Fire     : 101")
print("Ambulance: 108")

print("\nStay Safe!")
