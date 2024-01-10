import pandas as pd


# df = pd.read_csv("DataSets/youtube.csv")
df = pd.read_csv("C:\\Users\\BERNA\\OneDrive\\Masaüstü\\Python_Basics\\Veri_Analizi\\Pandas\\DataSets\\youtube.csv")

print('# 1- İlk 10 kaydı getiriniz.')
print(df.head(10))

print('# 2- İkinci 5 kaydı getiriniz.')
print(df[5:10])

print("# 3- Dataset' de bulunan kolon isimleri ve sayısını bulunuz.")
#1.Yol  
print(f'Kolon isimleri :  {list(df.columns.values)}')
print(f'Kolon sayısı :  {len(list(df.columns.values))}')
#2.Yol
print(df.columns)
print(len(df.columns))
print('# 4- Aşağıda bulunan bazı kolonları silin ve kalan kolonları listeleyiniz.')
# (thumbnail_link,comments_disabled,ratings_disabled,video_error_or_removed,description)
df.drop(["thumbnail_link","comments_disabled","ratings_disabled","video_error_or_removed","description","trending_date"],axis=1,inplace=True)
print(df.columns)

print('# 5- Beğenme (like) ve beğenmeme (dislike) sayılarının ortalamasını bulunuz.')
print(df["likes"].mean())
print(df["dislikes"].mean())

print('# 6- ilk 50 videonun like ve dislike kolonlarını getiriniz.')
print(df.head(50)[["title","likes","dislikes"]])

print('# 7- En çok görüntülenen video hangisidir ?')
# print(df['views'].max())
print(df[df["views"].max() == df["views"]]["title"].iloc[0])

print('# 8- En düşük görüntülenen video hangisidir?')
print(df[df["views"].min() == df["views"]]["title"].iloc[0])

print('# 9- En fazla görüntülenen ilk 10 video hangisidir ?')
print((df.sort_values(by='views')).head(10))

print('# 10- Kategoriye göre beğeni ortalamalarını sıralı şekilde getiriniz.')
print(df.groupby(['category_id'])['likes'].mean())

print('# 11- Kategoriye göre yorum sayılarını yukarıdan aşağıya sıralayınız.')
# print((df.groupby(['category_id'])["comment_count"].count()).sort_values())
print((df.groupby(['category_id'])["comment_count"].count().reset_index(name='comment_count_count')).sort_values(by='comment_count_count'))

print('# 12- Her kategoride kaç video vardır ?')
#1.Yol
print(df.groupby(['category_id'])['video_id'].count().reset_index(name='video_count'))
#2.Yol
print(df['category_id'].value_counts())

print('# 13- Her videonun title uzunluğu bilgisini yeni bir kolonda gösteriniz.')
print(df['title'].apply(len).reset_index(name='title_len'))

print('# 14- Her video için kullanılan tag sayısını yeni kolonda gösteriniz.')
df['tag_counts'] = df["tags"].apply(lambda x: len(x.split('|')))
print(df['tag_counts'])

print('# 15- En popüler videoları listeleyiniz.(like/dislike oranına göre)')
# print(df.groupby(['title']))
df['likes/dislikes rate'] = (df['likes']/df['dislikes'])
print(df[['title','likes/dislikes rate']].sort_values(by='likes/dislikes rate'))