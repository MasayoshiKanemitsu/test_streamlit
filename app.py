import streamlit as st
from PIL import Image
import pandas as pd

# streamlitのコンポーネントをお試し

st.title('Hello World!!')
st.caption('ここにテキストが入ります。')
st.subheader('自己紹介')
st.text('streamlitをimport\n'
        'titleを使う')

code = '''
import streamlit as st

st.title('Hello World!!')
'''
st.code(code, language='python')

# 画像
image = Image.open('python-logo.png')
st.image(image, width=400)

# テキストボックス
with st.form(key='profile_form'):
  name = st.text_input('名前')
  address = st.text_input('住所')
  # print(name)

  # セレクトボックス
  age_category = st.selectbox(
    '年齢層',
    ('子供','大人')
  )
  # 複数選択
  hobby = st.multiselect(
    '趣味',
    ('スポーツ','読書','プログラム','アニメ','漫画')
  )
  # ラジオボタン
  radioSelect = st.radio(
    'Yes / No',
    ('Yes','No')
  )

  # ボタン
  submit_btn = st.form_submit_button('送信')
  cancel_btn = st.form_submit_button('キャンセル')
  # ↑ボタンが押されている場合は「true」、押されていない場合は「false」を返す。
  # print(f'submit_btn: {submit_btn}')
  # print(f'cancel_btn: {cancel_btn}')

  if submit_btn:
    st.text(f'ようこそ！ {name}さん。{address}に荷物を送りました。')
    st.text(f'年齢層：{age_category}')
    st.text(f'趣味：{", ".join(hobby)}')


# CSV読み込み・表示・グラフ
df = pd.read_csv('./csv/data.csv',index_col='INDEX')
st.dataframe(df)
st.table(df)
st.line_chart(df)
st.bar_chart(df)
st.bar_chart(df['2021'])


# レイアウト
col1, col2 = st.columns(2)
with col1:
  st.table(df)
with col2:
  st.bar_chart(df)