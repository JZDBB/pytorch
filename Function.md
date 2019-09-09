# Function

### ConvTranspose2d

```python
class torch.nn.ConvTranspose2d(in_channels, out_channels, kernel_size, stride=1, padding=0, output_padding=0, groups=1, bias=True, dilation=1)
```

- `in_channels(int)` – 输入信号的通道数
- `out_channels(int)` – 卷积产生的通道数
- `kerner_size(int or tuple)` - 卷积核的大小
- `stride(int or tuple,optional)` - 卷积步长，即要将输入扩大的倍数。
- `padding(int or tuple, optional)` - 输入的每一条边补充0的层数，高宽都增加2*padding
- `output_padding(int or tuple, optional)` - 输出边补充0的层数，高宽都增加padding
- `groups(int, optional)` – 从输入通道到输出通道的阻塞连接数
- `bias(bool, optional)` - 如果bias=True，添加偏置
- `dilation(int or tuple, optional)` – 卷积核元素之间的间距

对于每一条边输入输出的尺寸的公式如下：

$output=(input-1) \times stride+outputpadding-2\times padding +kernelsize$

