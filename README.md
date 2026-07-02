---
license: apache-2.0
language:
- sr
---
<img  style="width:100%;" src="cover.png" class="cover">

<table style="width:100%;border-collapse:collapse;">
  <tr style="width:100%;">
    <td colspan=2 align=center>
      <h1>
        <span class="highlight-container">
          <span class="highlight">Srna Tokenizer</span>
        </span>
      </h1>
    </td>
  </tr>
  <tr style="width:100%;height:100%">
    <td width=50% valign=top>
      <h2>Opis (Srpski)</h2>
      <p><b>Срна</b> је специјализовани токенизатор за српски језик.</p>
      <p>Укључује неколико слојева нормализације у циљу уједначавања ћирилице и латинице и смањења броја редудантних токена.</p>
      <p>Покривена су три случаја:</p>
      <ul>
        <li><b>Компресија писма</b>: реч <code>текст</code> postaje <code>&lt;boc&gt; tekst&lt;eoc&gt;</code> приликом обраде, чувајући информацији о употреби писма, како би се у процесу декодирања извршила рестаурација.</li>
        <li><b>Компресија капитализације</b>: реч <code>Tekst</code> постаје <code>&lt;cap&gt; tekst</code>, чувајући потребне информације да би се текст реконстурисао, избегавајући засебне токене за <code>Tekst</code> и <code>tekst</code>.</li>
        <li><b>Компресија великих слова</b>: реч <code>TEKST</code> постаје <code>&lt;up&gt; tekst</code>, како би се избегло разбијање на појединачне карактере, притом чувајући инофмрације неопходне за рекоснтрукцију као и у претходним случајевима.</li>
      </ul>
      <p>Овај приступ изједначава латиницу и ћирилицу у моделу, смањујући дупликацију, олакшавајући учење и побољшавајући компресију кроз ослобађање места у вокабулару.</p>
      <p><b>Ограничење:</b> рестаурација ћирилице је комплексан задатак и захтева листу изузетака за диграфе (<code>dž</code>, <code>lj</code>, <code>nj</code> и у посебним случајевима <code>dj</code>). Овде су имплементиране до сада најпотпуније листе изузетака за српски језик, оформљене за потребе софтвера <a href="https://github.com/turanjanin/cirilizator/">Ћирилизатор</a>.</p>
    <p>Напомена: и постојећи токенизатори/модели се могу адаптирати. У том случају, је препоручено је искључивање компресије капитализације и великих слова, уколико се не ради дообучавање модела.</p>
    </td>
    <td width=50% valign=top>
      <h2>Description (English)</h2>
        <p><b>Srna</b> is a specialized tokenizer for the Serbian language.</p>
        <p>It includes several layers of normalization in order to equlaize Cyrillic and Latin scripts and reduce the number of redundant tokens.</p>
        <p>Three cases are covered:</p>
        <ul>
        <li><b>Script compression</b>: the word <code>text</code> becomes <code>&lt;boc&gt; text&lt;eoc&gt;</code> during processing, preserving information about the script usage, in order to perform restoration during the decoding process.</li>
        <li><b>Capitalization compression</b>: the word <code>Text</code> becomes <code>&lt;cap&gt; text</code>, preserving the information needed to reconstruct the text, avoiding separate tokens for <code>Text</code> and <code>text</code>.</li>
        <li><b>Uppercase compression</b>: the word <code>TEXT</code> becomes <code>&lt;up&gt; text</code>, to avoid breaking it into individual characters, while preserving the information necessary for reconstruction as in the previous cases.</li>
        </ul>
        <p>This approach equates Latin and Cyrillic in the model, reducing duplication, facilitating learning, and improving compression by freeing up space in the vocabulary.</p>
        <p><b>Limitation:</b> Cyrillic restoration is a complex task and requires a list of exceptions for digraphs (<code>dž</code>, <code>lj</code>, <code>nj</code> and in some cases <code>dj</code>). The most complete lists of exceptions for the Serbian language have been implemented here, designed for the needs of the <a href="https://github.com/turanjanin/cirilizator/">Cirilizator</a> software.</p>
        <p>Note: Existing tokenizers/models can also be adapted. In that case, it is recommended to turn off capitalization and uppercase compression unless fine-tuning of the model is being done.</p>    
    </td>
    </td>
  </tr>
</table>

---

## Употреба / Usage

```python
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("procesaur/Srna_tokenizer", trust_remote_code=True)

# Options
#tokenizer.case_compression=False
#tokenizer.script_compression=False
#tokenizer.omit_tags=True

text = "Pitao sam se 'да ли ће ме и рођени дјед и оџак надживети'?"

# Tokenize and print tokens
tokens = tokenizer.tokenize(text)
print(tokens)

# Encode to ids and decode back to string
ids = tokenizer.encode(text)
decoded = tokenizer.decode(ids)
print(decoded)

print(text==decoded)
```

```python
['<capi>', 'pita', 'o', 'Ġsam', 'Ġse', "Ġ'", '<csta>', 'da', 'Ġli', 'ĠÄĩe', 'Ġme', 'Ġi', 'ĠroÄĳeni', 'Ġdje', 'd', 'Ġnad', 'Å¾i', 'veti', "'", '?']
"Pitao sam se 'да ли ће ме и рођени дјед и оџак надживети'?"
True
```

<div class="inline-flex flex-col" style="line-height: 1.5;padding-right:50px">
  <div style="text-align: center; margin-top: 3px; font-size: 16px; font-weight: 800">Аутор / Author</div>
    <a href="https://huggingface.co/procesaur">  
      <div class="flex">
          <div
  			style="display:DISPLAY_1; margin-left: auto; margin-right: auto; width: 92px; height:92px; border-radius: 50%; 
            background-size: cover; background-image: url(&#39;https://cdn-uploads.huggingface.co/production/uploads/1673534533167-63bc254fb8c61b8aa496a39b.jpeg?w=200&h=200&f=face&#39;)">
          </div>
      </div>
    </a>
    <div style="text-align: center; font-size: 16px; font-weight: 800">Mihailo Škorić</div>
    <div>  
      <a href="https://huggingface.co/procesaur">
      	<div style="text-align: center; font-size: 14px;">@procesaur</div>
      </a>
    </div>
  </div>
</div>

Citation:

```bibtex
ускоро / soon
```

<div id="zastava">
  <div class="grb">
    <img src="https://www.ai.gov.rs/img/logo_60x120-2.png" style="position:relative; left:30px; z-index:10; height:85px">
  </div>
  <table width=100% style="border:0px">
    <tr style="background-color:#C6363C;width:100%;border:0px;height:30px"><td style="width:100vw"></td></tr>
    <tr style="background-color:#0C4076;width:100%;border:0px;height:30px"><td></td></tr>
    <tr style="background-color:#ffffff;width:100%;border:0px;height:30px"><td></td></tr>
  </table>
</div>

