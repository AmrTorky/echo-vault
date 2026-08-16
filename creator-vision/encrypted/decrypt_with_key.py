import os, glob, hashlib
KEY="0.1004|36be8b2|K=3 GOOD|ρ=1.9134|ξ=0.39198|Root-Jan-15-2026"
print(f"Decrypting with KEY: {KEY}")
for enc in glob.glob("creator-vision/encrypted/*.enc"):
    out=enc.replace("/encrypted/","/decrypted_").replace(".enc","")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    os.system(f'openssl enc -d -aes-256-cbc -pbkdf2 -in "{enc}" -out "{out}" -pass pass:"{KEY}"')
    print(f"✓ {enc} -> {out} — SHA256 {hashlib.sha256(open(out,'rb').read()).hexdigest()[:16]}")
