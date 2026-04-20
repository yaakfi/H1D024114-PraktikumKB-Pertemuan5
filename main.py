import tkinter as tk
from tkinter import ttk, messagebox

# Data Gejala
data_gejala = {
    "G1": "Nafas abnormal",
    "G2": "Suara serak",
    "G3": "Perubahan kulit",
    "G4": "Telinga penuh",
    "G5": "Nyeri bicara menelan",
    "G6": "Nyeri tenggorokan",
    "G7": "Nyeri leher",
    "G8": "Pendarahan hidung",
    "G9": "Telinga berdenging",
    "G10": "Airliur menetes",
    "G11": "Perubahan suara",
    "G12": "Sakit kepala",
    "G13": "Nyeri pinggir hidung",
    "G14": "Serangan vertigo",
    "G15": "Getah bening",
    "G16": "Leher bengkak",
    "G17": "Hidung tersumbat",
    "G18": "Infeksi sinus",
    "G19": "Beratbadan turun",
    "G20": "Nyeri telinga",
    "G21": "Selaput lendir merah",
    "G22": "Benjolan leher",
    "G23": "Tubuh tak seimbang",
    "G24": "Bolamata bergerak",
    "G25": "Nyeri wajah",
    "G26": "Dahi sakit",
    "G27": "Batuk",
    "G28": "Tumbuh dimulut",
    "G29": "Benjolan dileher",
    "G30": "Nyeri antara mata",
    "G31": "Radang gendang telinga",
    "G32": "Tenggorokan gatal",
    "G33": "Hidung meler",
    "G34": "Tuli",
    "G35": "Mual muntah",
    "G36": "Letih lesu",
    "G37": "Demam"
}

# Data Penyakit & Aturan (Rules)
data_penyakit = {
    "Tonsilitis": ["G37", "G12", "G5", "G27", "G6", "G21"],
    "Sinusitis Maksilaris": ["G37", "G12", "G27", "G17", "G33", "G36", "G29"],
    "Sinusitis Frontalis": ["G37", "G12", "G27", "G17", "G33", "G36", "G21", "G26"],
    "Sinusitis Edmoidalis": ["G37", "G12", "G27", "G17", "G33", "G36", "G21", "G30", "G13", "G26"],
    "Sinusitis Sfenoidalis": ["G37", "G12", "G27", "G17", "G33", "G36", "G29", "G7"],
    "Abses Peritonsiler": ["G37", "G12", "G6", "G15", "G2", "G29", "G10"],
    "Faringitis": ["G37", "G5", "G6", "G7", "G15"],
    "Kanker Laring": ["G5", "G27", "G6", "G15", "G2", "G19", "G1"],
    "Deviasi Septum": ["G37", "G17", "G20", "G8", "G18", "G25"],
    "Laringitis": ["G37", "G5", "G15", "G16", "G32"],
    "Kanker Leher & Kepala": ["G5", "G22", "G8", "G28", "G3", "G11"],
    "Otitis Media Akut": ["G37", "G20", "G35", "G31"],
    "Contact Ulcers": ["G5", "G2"],
    "Abses Parafaringeal": ["G5", "G16"],
    "Barotitis Media": ["G12", "G20"],
    "Kanker Nafasoring": ["G17", "G8"],
    "Kanker Tonsil": ["G6", "G29"],
    "Neuronitis Vestibularis": ["G35", "G24"],
    "Meniere": ["G20", "G35", "G14", "G4"],
    "Tumor Syaraf Pendengaran": ["G12", "G34", "G23"],
    "Kanker Leher Metastatik": ["G29"],
    "Osteosklerosis": ["G34", "G9"],
    "Vertigo Postular": ["G24"]
}

class AplikasiSistemPakar(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistem Pakar Diagnosa Penyakit THT - H1D024009")
        self.geometry("900x700")
        self.configure(bg="#f0f4f8")
        
        self.vars_gejala = {}
        
        self.create_widgets()

    def create_widgets(self):
        # Header
        header_frame = tk.Frame(self, bg="#2c3e50", pady=20)
        header_frame.pack(fill=tk.X)
        
        title = tk.Label(header_frame, text="Sistem Pakar Diagnosa Penyakit THT", 
                         font=("Helvetica", 20, "bold"), fg="white", bg="#2c3e50")
        title.pack()
        
        subtitle = tk.Label(header_frame, text="Centang gejala yang Anda alami untuk mendapatkan hasil diagnosa", 
                            font=("Helvetica", 11), fg="#ecf0f1", bg="#2c3e50")
        subtitle.pack()

        # Main frame with scrollbar
        main_frame = tk.Frame(self, bg="#f0f4f8")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        canvas = tk.Canvas(main_frame, bg="#f0f4f8", highlightthickness=0)
        scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
        
        scrollable_frame = tk.Frame(canvas, bg="#f0f4f8")
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Grid section for symptoms
        row_idx = 0
        col_idx = 0
        for doc_id, (kode, nama) in enumerate(data_gejala.items()):
            var = tk.IntVar()
            self.vars_gejala[kode] = var
            
            chk = tk.Checkbutton(scrollable_frame, text=f"[{kode}] {nama}", variable=var, 
                                 font=("Helvetica", 11), bg="#f0f4f8", activebackground="#f0f4f8", 
                                 anchor="w", width=35)
            chk.grid(row=row_idx, column=col_idx, sticky="w", padx=10, pady=5)
            
            col_idx += 1
            if col_idx > 1:
                col_idx = 0
                row_idx += 1

        # Diagnosa Button
        btn_frame = tk.Frame(self, bg="#f0f4f8", pady=10)
        btn_frame.pack(fill=tk.X, padx=20)
        
        btn_diagnosa = tk.Button(btn_frame, text="DIAGNOSA SEKARANG", font=("Helvetica", 13, "bold"), 
                                 bg="#3498db", fg="white", relief=tk.FLAT, padx=20, pady=10, 
                                 command=self.diagnosa)
        btn_diagnosa.pack(side=tk.RIGHT, padx=10)
        
        btn_reset = tk.Button(btn_frame, text="RESET", font=("Helvetica", 13, "bold"), 
                              bg="#e74c3c", fg="white", relief=tk.FLAT, padx=20, pady=10, 
                              command=self.reset_form)
        btn_reset.pack(side=tk.RIGHT)

    def diagnosa(self):
        # Ambil gejala yang dicentang
        gejala_dialami = [kode for kode, var in self.vars_gejala.items() if var.get() == 1]
        
        if not gejala_dialami:
            messagebox.showwarning("Peringatan", "Harap pilih minimal satu gejala terlebih dahulu!")
            return
            
        hasil_diagnosa = []
        
        # Hitung kecocokan tiap penyakit
        for penyakit, gejala_penyakit in data_penyakit.items():
            matched = set(gejala_dialami).intersection(set(gejala_penyakit))
            if matched:
                match_percentage = (len(matched) / len(gejala_penyakit)) * 100
                hasil_diagnosa.append({
                    "penyakit": penyakit,
                    "persentase": match_percentage,
                    "matched": matched
                })
        
        # Urutkan berdasarkan persentase tertinggi
        hasil_diagnosa.sort(key=lambda x: x["persentase"], reverse=True)
        
        self.tampilkan_hasil(hasil_diagnosa)

    def tampilkan_hasil(self, hasil_diagnosa):
        result_win = tk.Toplevel(self)
        result_win.title("Hasil Diagnosa")
        result_win.geometry("500x400")
        result_win.configure(bg="#ffffff")
        
        if not hasil_diagnosa:
            lbl = tk.Label(result_win, text="Tidak ditemukan penyakit yang cocok dengan gejala tersebut.", 
                           font=("Helvetica", 12), bg="white", fg="#e74c3c")
            lbl.pack(pady=20)
            return

        top_match = hasil_diagnosa[0]
        
        header = tk.Label(result_win, text="Kemungkinan Terbesar:", font=("Helvetica", 12), bg="white")
        header.pack(pady=(20, 5))
        
        lbl_penyakit = tk.Label(result_win, text=top_match["penyakit"], font=("Helvetica", 24, "bold"), 
                                fg="#2c3e50", bg="white")
        lbl_penyakit.pack()
        
        lbl_persen = tk.Label(result_win, text=f"Tingkat Kecocokan: {top_match['persentase']:.2f}%", 
                              font=("Helvetica", 12, "bold"), fg="#27ae60", bg="white")
        lbl_persen.pack(pady=5)
        
        lbl_detail = tk.Label(result_win, text=f"Gejala cocok: {len(top_match['matched'])} gejala.", 
                              font=("Helvetica", 10), bg="white", fg="#7f8c8d")
        lbl_detail.pack(pady=10)
        
        # Kemungkinan lain
        if len(hasil_diagnosa) > 1:
            frame_lain = tk.Frame(result_win, bg="#ecf0f1", padx=10, pady=10)
            frame_lain.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
            
            lbl_lain = tk.Label(frame_lain, text="Kemungkinan Lainnya:", font=("Helvetica", 11, "bold"), bg="#ecf0f1")
            lbl_lain.pack(anchor="w", pady=(0, 5))
            
            for i in range(1, min(4, len(hasil_diagnosa))):
                p = hasil_diagnosa[i]
                txt = f"- {p['penyakit']} ({p['persentase']:.1f}%)"
                lbl_p = tk.Label(frame_lain, text=txt, font=("Helvetica", 10), bg="#ecf0f1")
                lbl_p.pack(anchor="w")

        btn_tutup = tk.Button(result_win, text="TUTUP", bg="#34495e", fg="white", 
                              relief=tk.FLAT, padx=20, pady=5, command=result_win.destroy)
        btn_tutup.pack(pady=10)

    def reset_form(self):
        for var in self.vars_gejala.values():
            var.set(0)

if __name__ == "__main__":
    app = AplikasiSistemPakar()
    app.mainloop()
