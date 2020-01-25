string01 = """
<div class="animal">
    <p class="name">
		<a title="Tiger"></a>
    </p>
    <p class="content">
		Two tigers two tigers run fast
    </p>
</div>

<div class="animal">
    <p class="name">
		<a title="Rabbit"></a>
    </p>

    <p class="content">
		Small white rabbit white and white
    </p>
</div>
"""
import re

pattern = re.compile(r'<div class=".*?">.*?<p class=".*?">.*?<a title="(.*?)"></a>.*?</p>.*?<p class=".*?">(.*?)</p>.*?</div>', re.S)
result = pattern.findall(string01)
print(result)

tar_result = []
for r in range(len(result)):
    r0 = result[r][0].strip()
    r1 = result[r][1].strip()
    tar_result.append((r0,r1))

print(tar_result)





