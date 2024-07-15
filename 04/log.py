import numpy as np
import matplotlib.pyplot as plt

# データの作成
x = np.linspace(-0.1, 1, 100)  # 0.1から10までの100個の点を生成
y = np.log(x)  # xの自然対数を計算

# プロットの作成
plt.figure(figsize=(8, 6))  # 図のサイズを設定
plt.plot(x, y, linewidth=2, color='blue')  # ログプロットを描画

# 軸のラベルと題名の設定
plt.xlabel('x', fontsize=14)
plt.ylabel('log(x)', fontsize=14)
plt.title('Logarithmic Plot', fontsize=16)

# 軸の目盛りの設定
plt.tick_params(axis='both', labelsize=12)

# グリッドの表示
plt.grid(True)

# プロットの表示
plt.show()