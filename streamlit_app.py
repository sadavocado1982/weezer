import streamlit as st
from streamlit_tree_select import tree_select
import base64

# Function to create collapsible tree structure
def create_tree_structure():
    nodes = [
        {
            "label": "YouTube",
            "value": "folder_b",
            "children": [
                {"label": "How to make a YouTube video", "value": "sub_a"},
                {"label": "How to create a YouTube account", "value": "sub_b"},
                {"label": "How to publish your videos", "value": "sub_c"},
            ],
        },
        {
            "label": "how to cook a cake!",
            "value": "folder_c",
            "children": [
                {"label": "Ingredients", "value": "sub_d"},
                {
                    "label":  "bakeing",
                    "value": "folder_e",
                    "children": [
                        {"label": "Sub-sub-folder A", "value": "sub_sub_a"},
                        {"label": "Sub-sub-folder B", "value": "sub_sub_b"},
                    ],
                },
                {"label": "finish", "value": "sub_f"},
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

    # Set the background image
    background_image = """
            <style>
            [data-testid="stAppViewContainer"] > .main {
                background-image: url("https://scontent.fyaw1-1.fna.fbcdn.net/v/t39.30808-6/280496183_397664592227372_7839417422075289256_n.jpg?_nc_cat=102&ccb=1-7&_nc_sid=5f2048&_nc_ohc=vTrd1uIu3K0Ab6awg9q&_nc_ht=scontent.fyaw1-1.fna&oh=00_AfDCqGlDDi7ubQmBsn4t2oKHA6BUpAIX0SkqkBh558QKmA&oe=6629BA26");
                background-size: 100vw 100vh;  # This sets the size to cover 100% of the viewport width and height
                background-position: center;  
                background-repeat: no-repeat;
            }
            </style>
            """

    st.markdown(background_image, unsafe_allow_html=True)

    st.title("Interactive Tree Web App")

    # Toggle for kids mode
    kids_mode = st.checkbox("Kids Mode")

    # Update background and add smiling clouds if kids mode is activated
    if kids_mode:
        original_title = '<h1 style="font-family: sans-serif; color:black; font-size: 20px;">Kids mode activated!!✨ </h1>'
        st.markdown(original_title, unsafe_allow_html=True)

        # Set the background image
        background_image = """
        <style>
        [data-testid="stAppViewContainer"] > .main {
            background-image: url("https://p7.hiclipart.com/preview/975/564/23/rainbow-cloud-clip-art-rainbow-sun-painted-flowers.jpg");
            background-size: 100vw 100vh;  # This sets the size to cover 100% of the viewport width and height
            background-position: center;  
            background-repeat: no-repeat;
        }
        </style>
        """

        st.markdown(background_image, unsafe_allow_html=True)

    # Search bar
    search_query = st.text_input("Search for files")

    # Create collapsible tree structure
    return_select = tree_select(create_tree_structure())
    # st.write(return_select)

    # Handle double-click events
    # if st.session_state.clicked_file:
    #     download_file(st.session_state.clicked_file)


# Run the main function
if __name__ == "__main__":
    main()
