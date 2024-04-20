import streamlit as st


# Function to create collapsible tree structure
def create_tree_structure():
    # Mocking hierarchical structure
    st.write("Main Folder")
    with st.tree("Subfolder 1"):
        st.write("Leaf 1")
        st.write("Leaf 2")
    with st.tree("Subfolder 2"):
        st.write("Leaf 3")
        st.write("Leaf 4")


# Function to handle file download
def download_file(file_name):
    # Replace with actual download logic
    st.write(f"Downloading {file_name}")


# Main function
def main():
    st.title("Interactive Tree Web App")

    # Toggle for kids mode
    kids_mode = st.checkbox("Kids Mode")

    # Update background and add smiling clouds if kids mode is activated
    if kids_mode:
        st.write("Kids mode activated!")
        # Add code to update background and add smiling clouds

    # Search bar
    search_query = st.text_input("Search for files")

    # Create collapsible tree structure
    create_tree_structure()

    # Handle double-click events
    if st.session_state.clicked_file:
        download_file(st.session_state.clicked_file)


# Run the main function
if __name__ == "__main__":
    main()
