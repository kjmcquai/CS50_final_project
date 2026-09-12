# Import module to read csv files
import csv
# Import module for coordinate plotting on map
import matplotlib.pyplot as plt
# Import module to open and display image files
from PIL import Image


# Create a dictionary of location coordinates to plot migration routes
location_coords = {
    "alaska": (-155, 45),
    "canada": (-106, 40),
    "great lakes": (-85, 26),
    "gulf of mexico": (-90, 14),
    "prairies": (-105, 23),
    "southern u.s.": (-85, 18),
    "mexico": (-102, 12),
    "florida": (-81, 17),
    "south america": (-60, -30),
    "mid-atlantic": (-72, 25),
    "southeastern u.s.": (-80, 18),
    "canadian prairies": (-105, 32),
    "midwest usa": (-95, 23),
    "central america": (-90, 8),
    "northern u.s.": (-75, 24),
    "mississippi river valley": (-91, 20),
    "texas coast": (-98, 13),
    "chesapeake bay": (-77, 22)
}


# Create a dictionary to define abbriviations for months
month_aliases = {
    "jan": "january",
    "feb": "february",
    "mar": "march",
    "apr": "april",
    "may": "may",
    "jun": "june",
    "jul": "july",
    "aug": "august",
    "sep": "september",
    "oct": "october",
    "nov": "november",
    "dec": "december"
}


def main():
    # load migration data from CSV into dictionary
    data = load_duck_data("migration_data.csv")

    # Print an introduction message
    print("🦆 Welcome to Duck Migration Explorer!\n")

   # Keep asking for a valid species
    while True:
        species = input("Enter a duck species: ").strip().lower()
        species = species.replace("duck", "").strip()
        if species in data:
            break
        print(f"❌ Sorry, we don't have data for '{species}'. Please try again.")

    # Keep asking for a valid month
    while True:
        month_input = input("Enter a month: ").strip().lower()
        month = month_aliases.get(month_input[:3], month_input)
        if month in month_aliases.values():
            break
        print(f"❌ '{month_input}' is not a recognized month. Please try again.")

    # Look up the species in data
    duck = data.get(species)

    # Check the migration status of the species
    status = check_migration_status(duck, month)

    # Print a header for migration information
    print(f"\n📋 Migration Information for {species.capitalize()} Ducks:\n")

    # Print the migration information for status, months, route, and reason
    print(f"📍 Migration Status: {status}")
    print(f"📆 Migration Months: {', '.join(duck['migration_months']).title()}")
    print(f"🗺️  Route: {format_route(duck['route'])}")
    print(f"📝 Reason: {duck['reason']}")

    # Generate the migration route map
    generate_migration_map(species, duck["route"])


# Load in the CSV data into a dictionary, keyed by species name
def load_duck_data(filename):
    # Create a blank dict to store the data
    data = {}

    # Open the csv file
    with open(filename, newline='') as csvfile:
        # Use DictReader to read each row as a dictionary
        reader = csv.DictReader(csvfile)

        # Loop through the rows and format them accordingly
        for row in reader:
            species = row['species'].lower()
            migrates = row['migrates'].strip().lower() == 'true'
            months = [m.strip() for m in row['migration_months'].split(';') if m.strip()]
            route = [r.strip() for r in row['route'].split(';') if r.strip()]
            reason = row['reason'].strip()

            # Store the processed data in the dictionary under the species key
            data[species] = {
                'migrates': migrates,
                'migration_months': months,
                'route': route,
                'reason': reason,
            }

    # Return the full dictionary of collected data
    return data


# Determine if the species input migrates during the given month
def check_migration_status(duck, month):
    # If the species input does not migrate, print a message
    if not duck["migrates"]:
        return "Does not migrate"

    # If the month input is a migrating month, return that it is migrating
    elif month in duck["migration_months"]:
        return "Migrating"

    # If neither of those are true, return that the species is not migrating
    else:
        return "Not currently migrating"


# Format the migration route
def format_route(route_list):

    # If a migration route does not exist, print a message
    if not route_list:
        return "No migration route available."

    # If a route does exist, separate the locations with an arrow to show the migration route
    return " → ".join(route_list)


# Generate a map of the migration routes
def generate_migration_map(species, route):
    # Load the world map background image
    img = Image.open("world_map.png")

    # Create a matplotlib figure and axis for plotting points
    fig, ax = plt.subplots(figsize=(10, 5))

    # Display the map image on the plot, setting the coordinate system to longitude and latitude ranges
    ax.imshow(img, extent=[-180, 180, -90, 90])

    # Get coordinates for each location in route, skip unknown locations
    coords = [location_coords[loc.lower()] for loc in route if loc.lower() in location_coords]

    # If no valid coordinates are found, print a warning and exit the function
    if not coords:
        print("⚠️  No valid coordinates found for this migration route.")
        return

    # Separate the list of tuples into two lists: longitudes and latitudes
    lons, lats = zip(*coords)

    # Plot the migration route as a red line with dots on each stop
    ax.plot(lons, lats, marker='o', color='red', linestyle='--', linewidth=2)

    # Add title
    ax.set_title(f"{species.title()} Migration Route")

    # Hide axes for a cleaner look
    ax.axis('off')

    # Save the plot as an image file
    output_file = f"{species.lower().replace(' ', '_')}_migration.png"
    plt.savefig(output_file, bbox_inches='tight')

    # Close the plot to free up memory and avoid overlapping plots if called multiple times
    plt.close()

    # Inform the user that the migration map image has been saved successfully
    print(f"📷 Migration map saved as '{output_file}'")


# Call main
if __name__ == "__main__":
    main()
