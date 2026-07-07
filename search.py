from ddgs import DDGS
import webbrowser


def search(query):
    results_list = []

    print("\n" + "=" * 80)
    print(f"Searching for: {query}")
    print("=" * 80)

    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=10))

        if not results:
            print("\nNo results found.")
            return []

        for i, result in enumerate(results, start=1):
            title = result.get("title", "No Title")
            url = result.get("href") or result.get("url", "No URL")
            body = result.get("body", "No description available.")

            results_list.append({
                "title": title,
                "url": url,
                "body": body
            })

            print(f"\n[{i}] {title}")
            print(f"URL : {url}")
            print(f"Info: {body}")
            print("-" * 80)

    except Exception as e:
        print("\nAn error occurred while searching.")
        print(e)

    return results_list


def open_result(results):
    if not results:
        return

    while True:
        choice = input(
            "\nEnter result number to open (0 = Back, q = Quit): "
        ).strip().lower()

        if choice == "q":
            print("Goodbye!")
            exit()

        if choice == "0":
            return

        if choice.isdigit():
            num = int(choice)

            if 1 <= num <= len(results):
                print("\nOpening browser...")
                webbrowser.open(results[num - 1]["url"])
                return

        print("Invalid choice. Please try again.")


def main():
    print("=" * 80)
    print("             MINI SEARCH ENGINE")
    print("=" * 80)

    while True:
        query = input("\nSearch (or type 'exit'): ").strip()

        if query.lower() == "exit":
            print("\nThank you for using Mini Search Engine!")
            break

        if not query:
            print("Please enter something to search.")
            continue

        results = search(query)
        open_result(results)


if __name__ == "__main__":
    main()