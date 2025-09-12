import java.io.*;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.*;

public class Peminjaman {
    private static String currentFileName = "data-apr.txt";
    private static final SimpleDateFormat DATE_FORMAT = new SimpleDateFormat("d MMM", Locale.ENGLISH);

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.println("\n=== Sistem Manajemen Data Peminjaman ===");
            System.out.println("File aktif: " + currentFileName);
            System.out.println("1. Tambah Data");
            System.out.println("2. Lihat Data (Sorted by Tanggal)");
            System.out.println("3. Edit Status Data");
            System.out.println("4. Cari Pengisi List");
            System.out.println("5. Export ke CSV");
            System.out.println("6. Manajemen File");
            System.out.println("7. Keluar");
            System.out.print("Pilih menu (1-7): ");

            String pilihan = scanner.nextLine();
            switch (pilihan) {
                case "1":
                    tambahData(scanner);
                    break;
                case "2":
                    lihatData();
                    break;
                case "3":
                    editDataPeminjaman(scanner);
                    break;
                case "4":
                    lihatDataPengisiList(scanner);
                    break;
                case "5":
                    exportToCsv(scanner);
                    break;
                case "6":
                    manajemenFile(scanner);
                    break;
                case "7":
                    System.out.println("Program selesai. Bye, Mas!");
                    return;
                default:
                    System.out.println("Pilihan tidak valid, coba lagi!");
            }
        }
    }

    private static void manajemenFile(Scanner scanner) {
        while (true) {
            System.out.println("\n=== Manajemen File ===");
            System.out.println("File aktif: " + currentFileName);
            System.out.println("1. Buat File Baru");
            System.out.println("2. Pilih File yang Ada");
            System.out.println("3. Lihat Daftar File");
            System.out.println("4. Copy Data ke File Lain");
            System.out.println("5. Kembali ke Menu Utama");
            System.out.print("Pilih opsi (1-5): ");

            String pilihan = scanner.nextLine();
            switch (pilihan) {
                case "1":
                    buatFileBaru(scanner);
                    break;
                case "2":
                    pilihFile(scanner);
                    break;
                case "3":
                    lihatDaftarFile();
                    break;
                case "4":
                    copyDataKeFileLain(scanner);
                    break;
                case "5":
                    return;
                default:
                    System.out.println("Pilihan tidak valid!");
            }
        }
    }

    private static void buatFileBaru(Scanner scanner) {
        System.out.println("\nContoh format nama file:");
        System.out.println("- data-mei.txt");
        System.out.println("- data-jun.txt");
        System.out.println("- data-jul.txt");
        System.out.print("Masukkan nama file baru: ");
        String namaFile = scanner.nextLine();

        if (!namaFile.endsWith(".txt")) {
            namaFile += ".txt";
        }

        try {
            File file = new File(namaFile);
            if (file.createNewFile()) {
                currentFileName = namaFile;
                System.out.println("File baru berhasil dibuat: " + namaFile);
                System.out.println("File aktif sekarang: " + currentFileName);
            } else {
                System.out.println("File sudah ada. Gunakan menu 'Pilih File yang Ada' untuk beralih ke file tersebut.");
            }
        } catch (IOException e) {
            System.out.println("Gagal membuat file: " + e.getMessage());
        }
    }

    private static void pilihFile(Scanner scanner) {
        lihatDaftarFile();
        System.out.print("Masukkan nama file yang ingin dipilih: ");
        String namaFile = scanner.nextLine();

        File file = new File(namaFile);
        if (file.exists()) {
            currentFileName = namaFile;
            System.out.println("File aktif berubah ke: " + currentFileName);
        } else {
            System.out.println("File tidak ditemukan: " + namaFile);
        }
    }

    private static void lihatDaftarFile() {
        System.out.println("\n=== Daftar File Data ===");
        File currentDir = new File(".");
        File[] files = currentDir.listFiles((dir, name) -> name.startsWith("data-") && name.endsWith(".txt"));

        if (files != null && files.length > 0) {
            for (File file : files) {
                String status = file.getName().equals(currentFileName) ? " (AKTIF)" : "";
                System.out.println("- " + file.getName() + status);
            }
        } else {
            System.out.println("Tidak ada file data ditemukan.");
        }
    }

    private static void copyDataKeFileLain(Scanner scanner) {
        lihatDaftarFile();
        System.out.print("Copy dari file (kosongkan untuk file aktif): ");
        String sourceFile = scanner.nextLine();
        if (sourceFile.isEmpty()) {
            sourceFile = currentFileName;
        }

        System.out.print("Copy ke file: ");
        String targetFile = scanner.nextLine();

        if (!targetFile.endsWith(".txt")) {
            targetFile += ".txt";
        }

        try (BufferedReader reader = new BufferedReader(new FileReader(sourceFile));
             BufferedWriter writer = new BufferedWriter(new FileWriter(targetFile, true))) {

            String line;
            int count = 0;
            while ((line = reader.readLine()) != null) {
                writer.write(line);
                writer.newLine();
                count++;
            }
            System.out.println("Berhasil copy " + count + " baris data dari " + sourceFile + " ke " + targetFile);

        } catch (IOException e) {
            System.out.println("Gagal copy data: " + e.getMessage());
        }
    }

    private static void exportToCsv(Scanner scanner) {
        String csvFileName = currentFileName.replace(".txt", ".csv");

        try (BufferedReader reader = new BufferedReader(new FileReader(currentFileName));
             BufferedWriter writer = new BufferedWriter(new FileWriter(csvFileName))) {

            // Write CSV header
            writer.write("Nomor Data,Tanggal,Deadline,Nama,Barang,Pengisi List,Status Peminjaman");
            writer.newLine();

            String line;
            while ((line = reader.readLine()) != null) {
                if (!line.trim().isEmpty()) {
                    String csvLine = line.replace("|", ",");
                    writer.write(csvLine);
                    writer.newLine();
                }
            }
            System.out.println("Data berhasil diekspor ke: " + csvFileName);
            System.out.println("File CSV dapat dibuka di Excel atau Google Sheets.");

        } catch (IOException e) {
            System.out.println("Gagal export data: " + e.getMessage());
        }
    }

    private static void tambahData(Scanner scanner) {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(currentFileName, true))) {
            System.out.println("\n=== Input Data Peminjaman Masuk ===");

            int dataId = generateDataId();
            System.out.println("Nomor Data: " + dataId);

            System.out.print("Tanggal (1 Jan, 4 Jan, dst): ");
            String tanggal = scanner.nextLine();

            System.out.print("Deadline (1 Jan, 4 Jan, dst): ");
            String deadline = scanner.nextLine();

            System.out.print("Nama: ");
            String nama = scanner.nextLine();

            System.out.print("Barang: ");
            String barang = scanner.nextLine();

            System.out.print("Pengisi List: ");
            String pengisiList = scanner.nextLine();

            System.out.print("Status Peminjaman: ");
            String statusPeminjaman = scanner.nextLine();

            writer.write(dataId + "|" + tanggal + "|" + deadline + "|" + nama + "|" + barang + "|" + pengisiList + "|" + statusPeminjaman);
            writer.newLine();

            System.out.println("\nData berhasil disimpan ke " + currentFileName + "!");
        } catch (IOException e) {
            System.out.println("Terjadi kesalahan saat menyimpan data: " + e.getMessage());
        }
    }

    private static void lihatData() {
        System.out.println("\n=== Data Peminjaman (Sorted by Tanggal) ===");
        System.out.println("File: " + currentFileName);
        List<String> dataList = new ArrayList<>();

        try (BufferedReader reader = new BufferedReader(new FileReader(currentFileName))) {
            String line;
            while ((line = reader.readLine()) != null) {
                if (!line.trim().isEmpty()) {
                    dataList.add(line);
                }
            }
        } catch (FileNotFoundException e) {
            System.out.println("Belum ada data yang tersimpan di " + currentFileName);
            return;
        } catch (IOException e) {
            System.out.println("Terjadi kesalahan saat membaca data: " + e.getMessage());
            return;
        }

        // Sort list with  custom comparator
        Collections.sort(dataList, new Comparator<String>() {
            @Override
            public int compare(String d1, String d2) {
                String[] data1 = d1.split("\\|");
                String[] data2 = d2.split("\\|");
                try {
                    Date tanggal1 = DATE_FORMAT.parse(data1[1]);
                    Date tanggal2 = DATE_FORMAT.parse(data2[1]);
                    return tanggal1.compareTo(tanggal2);
                } catch (ParseException e) {
                    return 0;
                }
            }
        });

        // Show sorted data
        for (String data : dataList) {
            String[] parts = data.split("\\|");
            if (parts.length == 7) {
                System.out.println("Nomor Data: " + parts[0]);
                System.out.println("Tanggal: " + parts[1]);
                System.out.println("Deadline: " + parts[2]);
                System.out.println("Nama: " + parts[3]);
                System.out.println("Barang: " + parts[4]);
                System.out.println("Pengisi List: " + parts[5]);
                System.out.println("Status Peminjaman: " + parts[6]);
                System.out.println("----------------------------------");
            }
        }
    }

    private static void editDataPeminjaman(Scanner scanner) {
        List<String> dataList = new ArrayList<>();
        try (BufferedReader reader = new BufferedReader(new FileReader(currentFileName))) {
            String line;
            while ((line = reader.readLine()) != null) {
                dataList.add(line);
            }
        } catch (IOException e) {
            System.out.println("Terjadi kesalahan saat membaca data: " + e.getMessage());
            return;
        }

        if (dataList.isEmpty()) {
            System.out.println("Belum ada data yang tersimpan.");
            return;
        }

        System.out.print("Masukkan Nomor Data yang ingin diedit: ");
        String nomorDataEdit = scanner.nextLine();

        boolean found = false;
        for (int i = 0; i < dataList.size(); i++) {
            String[] parts = dataList.get(i).split("\\|");
            if (parts[0].equals(nomorDataEdit)) {
                System.out.println("\n=== Edit Data Peminjaman (Nomor Data: " + parts[0] + ") ===");
                System.out.println("1. Tanggal: " + parts[1]);
                System.out.println("2. Deadline: " + parts[2]);
                System.out.println("3. Nama: " + parts[3]);
                System.out.println("4. Barang: " + parts[4]);
                System.out.println("5. Pengisi List: " + parts[5]);
                System.out.println("6. Status Peminjaman: " + parts[6]);
                System.out.print("Pilih nomor field yang ingin diedit (1-6): ");

                String pilihanFieldInput = scanner.nextLine();
                int pilihanField;
                try {
                    pilihanField = Integer.parseInt(pilihanFieldInput);
                } catch (NumberFormatException e) {
                    System.out.println("Input tidak valid. Harus berupa angka.");
                    return;
                }

                if (pilihanField >= 1 && pilihanField <= 6) {
                    System.out.print("Masukkan Data baru: ");
                    String nilaiBaru = scanner.nextLine();
                    parts[pilihanField] = nilaiBaru; // Note: parts[0] is Nomor Data, so index starts from 1
                    dataList.set(i, String.join("|", parts));

                    try (BufferedWriter writer = new BufferedWriter(new FileWriter(currentFileName))) {
                        for (String data : dataList) {
                            writer.write(data);
                            writer.newLine();
                        }
                        System.out.println("Data berhasil diperbarui!");
                    } catch (IOException e) {
                        System.out.println("Terjadi kesalahan saat menyimpan data: " + e.getMessage());
                    }
                } else {
                    System.out.println("Pilihan field tidak valid.");
                }
                found = true;
                break;
            }
        }

        if (!found) {
            System.out.println("Nomor Data tidak ditemukan.");
        }
    }

    private static int generateDataId() {
        return new Random().nextInt(100);
    }

    private static void lihatDataPengisiList(Scanner scanner) {
        System.out.print("Masukkan nama Pengisi List: ");
        String namaPengisiList = scanner.nextLine();

        List<String> dataList = new ArrayList<>();
        try (BufferedReader reader = new BufferedReader(new FileReader(currentFileName))) {
            String line;
            while ((line = reader.readLine()) != null) {
                dataList.add(line);
            }
        } catch (IOException e) {
            System.out.println("Terjadi kesalahan saat membaca data: " + e.getMessage());
            return;
        }

        boolean found = false;
        boolean headerPrinted = false;

        for (String data : dataList) {
            String[] parts = data.split("\\|");
            if (parts.length == 7 && parts[5].equalsIgnoreCase(namaPengisiList)) {
                if (!headerPrinted) {
                    System.out.println("\n=== Data Peminjaman oleh " + namaPengisiList + " ===");
                    headerPrinted = true;
                }
                System.out.println("Barang: " + parts[4]);
                System.out.println("Tanggal: " + parts[1]);
                System.out.println("Status Peminjaman: " + parts[6]);
                System.out.println("----------------------------------");
                found = true;
            }
        }

        if (!found) {
            System.out.println("Tidak ada data peminjaman yang ditemukan untuk Pengisi List: " + namaPengisiList);
        }
    }
}
