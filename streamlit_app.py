import streamlit as st
from streamlit_tree_select import tree_select

# Function to create collapsible tree structure
def create_tree_structure():
    nodes = [
        {"label": "Folder A", "value": "folder_a"},
        {
            "label": "Folder B",
            "value": "folder_b",
            "children": [
                {"label": "Sub-folder A", "value": "sub_a"},
                {"label": "Sub-folder B", "value": "sub_b"},
                {"label": "Sub-folder C", "value": "sub_c"},
            ],
        },
        {
            "label": "Folder C",
            "value": "folder_c",
            "children": [
                {"label": "Sub-folder D", "value": "sub_d"},
                {
                    "label": "Sub-folder E",
                    "value": "sub_e",
                    "children": [
                        {"label": "Sub-sub-folder A", "value": "sub_sub_a"},
                        {"label": "Sub-sub-folder B", "value": "sub_sub_b"},
                    ],
                },
                {"label": "Sub-folder F", "value": "sub_f"},
            ],
        },
    ]
    return nodes


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
        # Add CSS to set background image
        st.markdown(
            """
            <style>
            body {
                background-image: url("assets/rainbow_nonsense.png");
                background-size: cover;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )

    # Search bar
    search_query = st.text_input("Search for files")

    # Create collapsible tree structure
    return_select = tree_select(create_tree_structure())
    st.write(return_select)

    # Handle double-click events
    # if st.session_state.clicked_file:
    #     download_file(st.session_state.clicked_file)


# Run the main function
if __name__ == "__main__":
    main()