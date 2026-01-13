import tkinter as tk

def speed():
    d = float(distance.get())
    t = float(time.get())
    result.set(f"Speed = {d/t:.2f} m/s")

def force():
    m = float(mass.get())
    a = float(acc.get())
    result.set(f"Force = {m*a:.2f} N")

def energy():
    m = float(mass.get())
    v = float(vel.get())
    result.set(f"Kinetic Energy = {0.5*m*v*v:.2f} J")

app = tk.Tk()
app.title("Physics Formula Solver")
app.geometry("350x400")

tk.Label(app, text="Distance (m)").pack()
distance = tk.Entry(app)
distance.pack()

tk.Label(app, text="Time (s)").pack()
time = tk.Entry(app)
time.pack()

tk.Button(app, text="Calculate Speed", command=speed).pack(pady=5)

tk.Label(app, text="Mass (kg)").pack()
mass = tk.Entry(app)
mass.pack()

tk.Label(app, text="Acceleration (m/s²)").pack()
acc = tk.Entry(app)
acc.pack()

tk.Button(app, text="Calculate Force", command=force).pack(pady=5)

tk.Label(app, text="Velocity (m/s)").pack()
vel = tk.Entry(app)
vel.pack()

tk.Button(app, text="Calculate Energy", command=energy).pack(pady=5)

result = tk.StringVar()
tk.Label(app, textvariable=result, font=("Arial", 12)).pack(pady=10)

app.mainloop()
