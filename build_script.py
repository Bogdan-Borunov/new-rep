import os

output_dir = 'public'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

with open(os.path.join(output_dir, 'index.html'), 'w') as f:
    f.write('<html><body><h1>Hello, Netlify!</h1></body></html>')

print("Build completed!")
