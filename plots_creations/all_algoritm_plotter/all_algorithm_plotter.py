import matplotlib.pyplot as plt
import pandas as pd
import os
import glob

def main():
    folder_path = "C://Users//danny//Desktop//Sorting_Algorithms_Research//time_csvs"

    save_folder = "C://Users//danny//Desktop//Sorting_Algorithms_Research//plots//plots_of_algo_comparisons"
    os.makedirs(save_folder, exist_ok=True)

    csv_files = glob.glob(os.path.join(folder_path, '*.csv'))

    for csv_file in csv_files:
        file_name_with_ext = csv_file.split('\\')[-1]
        file_name = file_name_with_ext.split('.')[0]

        df = pd.read_csv(csv_file)

        plt.figure(figsize=(10,6))

        for column in df.columns:
            plt.plot(df.index, df[column], marker='o', label=column)

        plt.title(file_name)
        plt.xlabel('Test Case Index')
        plt.ylabel('Time (seconds)')
        plt.legend()
        plt.grid(True)

        save_path = os.path.join(save_folder, f'{file_name}.png')
        plt.savefig(save_path)

        plt.close()

if __name__ == "__main__":
    main()