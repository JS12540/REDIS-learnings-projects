import os
import streamlit as st
import redis
import pdfplumber

# Connect to Redis
r = redis.Redis(host='localhost', port=6379, db=0)

# Function to index documents
def index_documents(folder_path):
    st.write("Indexing documents...")
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.pdf'):
                file_path = os.path.join(root, file)
                with pdfplumber.open(file_path) as pdf:
                    text = ""
                    for page in pdf.pages:
                        text += page.extract_text()
                    words = text.split()
                    for word in words:
                        # Index each word with the reference to the document
                        r.sadd(word.lower(), file_path)
    st.write("Indexing complete.")

# Function to search documents
def search_documents(query):
    st.write("Searching for documents...")
    # Check if the query is already cached
    cached_results = r.get(query.lower())
    if cached_results:
        st.write("Using cached results for query:", query)
        return cached_results.decode().split(',')
    
    # If not cached, perform the search
    results = set()
    keywords = query.lower().split()
    for keyword in keywords:
        documents = r.smembers(keyword)
        if documents:
            results.update(documents)
    # Cache the results
    
    r.set(query.lower(), str(list(results)))
    
    st.write("Search complete.")
    return results

# Function to rank search results
def rank_results(results):
    # Implement ranking algorithm here
    # For example: sort results based on the number of matched keywords
    return sorted(results, key=lambda x: len(x), reverse=True)

# Function to display results in Streamlit
def display_results(results):
    st.write("Displaying search results:")
    for result in results:
        st.write(result)

# Main Streamlit app
def main():
    st.title("PDF Search Engine")
    folder_path = "//home/elixirnlp0/Downloads/Prototype_Data"
    
    # Index documents on app startup
    index_documents(folder_path)

    query = st.text_input("Enter your query:")
    if query:
        # Check if the query is already cached
        cached_results = search_documents(query)
        ranked_results = rank_results(cached_results)
        display_results(ranked_results)

if __name__ == "__main__":
    main()
