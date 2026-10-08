def printing(unprited_docs,printed_docs):

    while unprited_docs:
        current_doc = unprited_docs.pop()
        print(f"Currently printing doc: {current_doc}")
        printed_docs.append(current_doc)

def show_completed_model(printed_docs):
    print("\nFollowing are the docs whose printing is done: ")
    for i in printed_docs:
        print(i)