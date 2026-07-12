import os
import fitz  


class DocumentLoader:

    def __init__(self, data_folder="data"):
        self.data_folder = data_folder

    def load_documents(self):

        documents = []

        pdf_count = 0
        txt_count = 0
        total_pages = 0

        if not os.path.exists(self.data_folder):
            raise FileNotFoundError(
                f"Folder '{self.data_folder}' not found."
            )

        files = os.listdir(self.data_folder)

        if not files:
            print("No documents found inside the data folder.")
            return documents

        print("\n========== LOADING DOCUMENTS ==========\n")

        for file in files:

            file_path = os.path.join(self.data_folder, file)

            if not os.path.isfile(file_path):
                continue

            if file.lower().endswith(".pdf"):

                pdf = fitz.open(file_path)

                pdf_count += 1

                print(f"Loading PDF : {file}")

                for page_num in range(len(pdf)):

                    page = pdf.load_page(page_num)

                    text = page.get_text()

                   
                    if text.strip():

                        documents.append(
                            {
                                "text": text,
                                "source": file,
                                "page": page_num + 1,
                            }
                        )

                total_pages += len(pdf)

                pdf.close()

   

            elif file.lower().endswith(".txt"):

                txt_count += 1

                print(f"Loading TXT : {file}")

                with open(
                    file_path,
                    "r",
                    encoding="utf-8"
                ) as f:

                    text = f.read()

                if text.strip():

                    documents.append(
                        {
                            "text": text,
                            "source": file,
                            "page": 1,
                        }
                    )

            else:

                print(f"Skipping unsupported file : {file}")

        print("\n========== DOCUMENT STATISTICS ==========")
        print(f"PDF Files        : {pdf_count}")
        print(f"TXT Files        : {txt_count}")
        print(f"Total Documents  : {pdf_count + txt_count}")
        print(f"Total Pages      : {total_pages}")
        print(f"Page/Doc Entries : {len(documents)}")
        print("=========================================\n")

        return documents