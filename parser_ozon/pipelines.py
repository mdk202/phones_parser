import pandas as pd


class ParserOzonPipeline:
    items = []

    def process_item(self, item, spider):
        item.setdefault('version', 'None')
        self.items.append(item)
        return item

    def close_spider(self, spider):
        df = pd.DataFrame(self.items)
        distribution = df.value_counts()
        with open('result.txt', 'w') as file:
            result = distribution.to_string(header=False)
            file.write(result)
        print(result)
