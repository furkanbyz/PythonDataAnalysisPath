import pandas as pd
import numpy as np

# DETECTING MISSING DATAS
result = np.nan
result = pd.isnull(np.nan)
# nan değeri null mudur? True döner.
result = pd.isnull(None)
# none değeri null mudur? True döner.
result = pd.isna(None) 
# isna ve isnull aynı işe yarar denilebilir.
result = pd.notnull(None) 
# false döner
result = pd.notnull(3) 
# 3 değeri not null mıdır? True döner.
result = pd.notna(3) # notnull ile aynı çıktıyı verir.
#  isnull ve isna fonk. tersleri de notnull ve notna'dır.


# FILTERING MISSING DATAS
result = pd.isnull(pd.Series([1,np.nan,7])) 
# hangileri nulldır diye sorar, false true false döner.
result = pd.notnull(pd.Series([1,np.nan,7])) 
# hangileri null değildir diye sorar, true false true döner
result = pd.isnull(pd.DataFrame({
    'Column A': [1, np.nan, 7],
    'Column B': [np.nan, 2, 3],
    'Column C': [np.nan, 2, np.nan]
}))
# değerlere tek tek null mıdır diye sorar
# isna ve isnull aynı çıktıyı verir.

s = pd.Series([1, 2, 3, np.nan, np.nan, 4])
result = pd.notnull(s)
# not null olan değerlere true, diğerlerine false verir.
result = pd.notnull(s).sum()
# kaç tane not null olan değer var diye sorar. 4 döndürür
result = pd.isnull(s) # notnull()'ın tersi sonuç verir.
result = pd.isnull(s).sum() # 2 döndürür.


# DROPPING NULL VALUES
result = s.dropna()
# nan değerleri çıkarıp, 4 indexli yeni bir seri döndürür.


df = pd.DataFrame({
    'Column A': [1, np.nan, 30, np.nan],
    'Column B': [2, 8, 31, np.nan],
    'Column C': [np.nan, 9, 32, 100],
    'Column D': [5, 8, 34, 110],
})

result = pd.isnull(df) # tek tek null mu diye kontrol eder
result = pd.isnull(df).sum() # her kolonda kaç null değer var diye sorar

result = df.dropna(axis=1)  # axis='columns' also works, nan değer içeren kolonları siler yalnızca column D döner
result = df.dropna(how='any')  # default behavior, yalnızca column 2 döner
result = df.dropna(how='all') # ?
result = df.dropna(thresh=2) # ?


s = pd.Series([1, 2, 3, np.nan, np.nan, 4])
result = s.fillna(0) # nan değerleri 0 ile doldurur
result = s.fillna(s.mean()) # nan değerleri ortalama ile doldurur
result = s.fillna(method="ffill") # null değerleri son null olmayan değer ile doldurur
result = s.fillna(method="bfill") # null değerleri sonraki null olmayan değer ile doldurur

result = df.fillna(method="ffill", axis=0) # null değerleri kolon bazında son null olmayan değer ile doldurur
result = df.fillna(method="ffill", axis=1) # null değerleri satır bazında son null olmayan değer ile doldurur

result = df.count() # kolon bazında null olmayan değerlerin sayısını verir


# CLEANING NOTNULL VALUES
df = pd.DataFrame({
    'Sex': ['M', 'F', 'F', 'D', '?'],
    'Age': [29, 30, 24, 290, 25],
})

result = df['Sex'].unique() # sex kolonundaki unique değerleri listeler
result = df['Sex'].value_counts() # kaçar tane sex değişkeninden bulunuyor diye sorar
result = df['Sex'].replace('D', 'F') # sex kolonundaki D'yi F ile değiştirdi
result = df['Sex'].replace({'D': 'F', 'M': 'N'}) # D'yi F, M'yi N ile değiştirdi
result = df.replace({ # değiştirme işlemi birçok parametreye göre yapıldı
    'Sex': {
        'D': 'Female',
        'M': 'Male',
        'F': 'Female',
        '?': 'not known'
    },
    'Age': {
        290: 29
    }
})


print(df)
print(result)
