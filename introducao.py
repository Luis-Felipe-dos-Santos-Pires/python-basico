import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO
import base64

x = np.linspace(0, 2 * np.pi, 200)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
image = BytesIO()
plt.savefig(image, format='png')
print(base64.b64encode(image.getvalue()))
plt.show()