from auth.login import login
from security.authz import authorize
from security.validation import sanitize_output


def run_app():
    print("SAFEVAULT - APP RUN")

    user = login("admin", "Admin123")

    if user:
        print("Login exitoso")

        if authorize(user, "admin"):
            print("Acceso admin permitido")
        else:
            print("Acceso denegado")
    else:
        print("Credenciales incorrectas")


def demo_xss_protection():
    print("\n=== XSS DEMO ===")

    malicious = "<script>alert('hack')</script>"
    safe = sanitize_output(malicious)

    print("Original:", malicious)
    print("Seguro:", safe)


if __name__ == "__main__":
    run_app()
    demo_xss_protection()