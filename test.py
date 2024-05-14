import dash
import dash_bootstrap_components as dbc
# import dash_core_components as dcc
from dash import dcc
#import plotly.io as pio
import plotly.offline as pyo
#import dash_html_components as html
from dash import html
from dash.dependencies import Input, Output, State
from plotly.subplots import make_subplots
from tqdm import tqdm

import pandas as pd
import numpy as np
from datetime import datetime as dt
from datetime import timedelta
import plotly.figure_factory as ff
import plotly.graph_objects as go
import pathlib
import shutil
import os
import xlrd
import xlsxwriter
import openpyxl

df_1=pd.read_csv('./datasets/CSV/TE Data/DM Data.csv',parse_dates=['Month'])

df_filter=df_1.loc[df_1['Month'] == dt.today().replace(hour=0, minute=0, second=0, microsecond=0) -timedelta(days=10), ['3 CSR', '4 CSR']].reset_index( drop=True)
print(df_filter)
# workbook = xlsxwriter.Workbook(r'C:\Users\1022794\Desktop\AHC\A2.xlsx')
# existingWorksheet = workbook.get_worksheet_by_name('Sheet1')
# print(workbook.worksheets())
# existingWorksheet.write_row(0,0,'xyz')
#
# workbook.close()
# path=r'C:\Users\1022794\Desktop\SigmaEyeConverter\AHC'
# py = pathlib.Path(path).glob("*.ahc")
# for file in py:
#     base = os.path.splitext(file)[0]
#     os.rename(file, base + '.csv')
#
# path=r'C:\Users\1022794\Desktop\SigmaEyeConverter\AHC'
# csv = pathlib.Path(path).glob("*.csv")
# for file in csv:
#     df=pd.read_csv(file)
#     date=df.columns[0]
#     time=df.iloc[0,0]
#     number1=df.iloc[3,0]
#     number2=df.iloc[4,0]

    # df1=df.iloc[12:,:].reset_index(drop=True)
    # a=2
    # temp=[]
    # while a<df1.shape[0]:
    #     temp.append(int(df1.iloc[a,0]))
    #     a+=4
    # b=0
    # status=[]
    # while b<df1.shape[0]:
    #     status.append(df1.iloc[b,0])
    #     b+=4
    #
    # c=1
    # Emissivity=[]
    # while c<df1.shape[0]:
    #     Emissivity.append(float(df1.iloc[c,0]))
    #     c+=4
    #
    # d=3
    # Thermocouple=[]
    # while d<df1.shape[0]:
    #     Thermocouple.append(int(df1.iloc[d,0]))
    #     d+=4
    # # df=pd.read_excel('sample1.xls', engine='xlrd')
    # df_main=pd.DataFrame({'No':[i for i in range(1, len(status)+1)], 'Status':status, 'Emissivity':Emissivity, 'Thermometer': temp, 'Thermocouple':Thermocouple})
    # # df_main.to_excel(r'C:\Users\1022794\Desktop\AHC\output.xlsx', index=False)
    # temp=df_main['Thermometer'].tolist()
    # temp_arr=np.array(temp)
    # max_temp=temp_arr.max()
    # min_temp=temp_arr.min()
    # mean_temp=temp_arr.mean().round(2)
    # wb=openpyxl.load_workbook(r'C:\Users\1022794\Desktop\AHC\A2.xlsx')
    # sheet=wb['Sheet1']
    #
    # for x in range(292):
    #     sheet['D{}'.format(x+2)]=temp[x]
    #
    # sheet['H1']=date
    # sheet['H2']=date
    # sheet['H3']=time
    # sheet['H8']=max_temp
    # sheet['H9']=min_temp
    # sheet['H10']=mean_temp
    #
    # wb.save(r'C:\Users\1022794\Desktop\AHC\Output.xlsx')

# print('Success!')
# print('Successful')
# df=pd.read_excel('sample.xlsx',sheet_name='TTR', engine='openpyxl')
#
# df.dropna(inplace=True, thresh=1)
# df=df.iloc[0:2001,30:38]
#
# # df=df.iloc[2079:,27:36]
# df.reset_index(inplace=True, drop=True)
# # file = xlrd.open_workbook('sample.xlsx', encoding_override="latin-1")
#
# a=0
# b=76
# all_df=[]
# while b <= 2000:
#     df_filter=df.iloc[a:b,:]
#     all_df.append(df_filter)
#
#     a=b
#     b+=77
#
# # a=0
# # b=74
# # all_df=[]
# # while b <= 2000:
# #     df_filter=df.iloc[a:b,:]
# #     all_df.append(df_filter)
# #
# #     a=b
# #     b+=76
# # #
# #
# # print(len(all_df))
# # print(all_df[2])
# for i in range(len(all_df)):
#     # print(all_df[i].iloc[0,0])
#     print(all_df[i])
#
# def dateswap(x):
#     a=x.split('-')
#     if len(a[-1])==4:
#         a[0],a[2]=a[2],a[0]
#     return '{}-{}-{}'.format(a[0],a[1],a[2])
#
# for x in tqdm(range(4),desc='Compiling cokefall & amperage...'):
#     df=pd.read_csv('./datasets/CSV/Battery{}/Pushing-report.csv'.format(x+5))
#     df_1=df[['Date', 'Oven No.', 'Amperage', 'Cake Ht.', 'Cokefall', 'Smoke', 'front_side', 'back_side', 'lock_slip', 'Act. CPD']]
#     df_1['Date']=df_1['Date'].apply(lambda x: dateswap(x))
#     df_1['Date']=df_1['Date'].apply(lambda x: dt.strptime(x, '%Y-%m-%d')).copy()
#     # df_1=df_1[df_1['Date'] == date]
#
#     #cokefall with cpd DataFrame
#     df_cokefall=df_1.loc[df_1['Cokefall'] == 'YES', ['Oven No.', 'Date', 'Cokefall', 'Act. CPD']]

# df_blend=pd.read_excel('/process_data/TE Data/DM Data.xlsx', sheet_name='Blend', header=[2])
# print(df_blend)
# df=pd.read_excel('/process_data/TE Data/DM Data.xlsx', sheet_name='Data', header=[2])
# def te_Data():
#     try:
#         df=pd.read_excel('/process_data/TE Data/DM Data.xlsx', sheet_name='Data', header=None)
#         df_blend=pd.read_excel('/process_data/TE Data/DM Data.xlsx', sheet_name='Blend')

#         df.to_csv('./datasets/CSV/TE Data/DM Data.csv')
#         df_blend.to_csv('./datasets/CSV/TE Data/DM Data_blend.csv')

#     except:
#         pass


# skiprows=[i for i in range(703)]
# del skiprows[2]
# # print(skiprows)
# df4=pd.read_excel('/process_data/pushing_rp_backup/Master/Master file 1 - FY19-20.xlsx', sheet_name='CO 4', header=[0], skiprows=skiprows)
# df4.rename(columns={'Unnamed: 0':'Date', 'Monthly Plan':'4 MP', 'Unnamed: 10':'4 Prod Actual', 'Unnamed: 5':'4 Pushings', 'Yield':'4 Yield'}, inplace=True)
# df4=df4.loc[3:, ['Date', '4 MP', '4 Prod Actual', '4 Pushings', '4 Yield']].reset_index(drop=True)
# print(df4)
# print(df4.loc[:, ['4 MP', '4 Prod Actual', '4 Pushings', '4 Yield']])

# print(df.head(20))
# print(df.to_csv('sample1.csv'))
# def copy_master():
#
#     source_dst=r'\\JSWSL-VJN-D2621\tcg on 10.10.39.125\Master file\Master file 1 - FY19-20.xlsx'
#     target=r'C:\Projects\datasets\Master'
#     shutil.copy(source_dst, target)
#
#
# if __name__ == '__main__':
#     copy_master()
# graph=n['points'][0][0]['curveNumber']
#
# if graph in [0, 1]:
#     df=pd.read_csv('./datasets/CSV/Battery5/shiftwise_temp.csv')
#     df['Date']=df['Date'].apply(lambda x: dt.strptime(x, '%Y-%m-%d'))
#     df_current=df[df['Date']==dt(2021,12,1)]
#
#     trace1=go.Bar(
#     x='P_A1',
#     y=df_current['P_A1'].astype(int)
#     )
#     trace2=go.Bar(
#     x='P_A2',
#     y=df_current['P_A2'].astype(int)
#     )
#     trace3=go.Bar(
#     x='P_B1',
#     y=df_current['P_B1'].astype(int)
#     )
#     trace4=go.Bar(
#     x='P_B2',
#     y=df_current['P_B2'].astype(int)
#     )
#     trace5=go.Bar(
#     x='P_C1',
#     y=df_current['P_C1'].astype(int)
#     )
#     trace6=go.Bar(
#     x='P_C2',
#     y=df_current['P_C2'].astype(int)
#     )
#
#     trace11=go.Bar(
#     x='A1_p',
#     y=df_current['A1_p'].astype(int)
#     )
#     trace22=go.Bar(
#     x='A2_p',
#     y=df_current['A2_p'].astype(int)
#     )
#     trace33=go.Bar(
#     x='C_B1',
#     y=df_current['C_B1'].astype(int)
#     )
#     trace44=go.Bar(
#     x='C_B2',
#     y=df_current['C_B2'].astype(int)
#     )
#     trace55=go.Bar(
#     x='C_C1',
#     y=df_current['C_C1'].astype(int)
#     )
#     trace66=go.Bar(
#     x='C_C2',
#     y=df_current['C_C2'].astype(int)
#     )
#
#     fig1=go.Figure(data=[trace1, trace2, trace3, trace4, trace5, trace6])
#     fig2=go.Figure(data=[trace11, trace22, trace33, trace44, trace55, trace66])
#
# elif graph in [2, 3]:
#     df=pd.read_csv('./datasets/CSV/Battery6/shiftwise_temp.csv')
#     df['Date']=df['Date'].apply(lambda x: dt.strptime(x, '%Y-%m-%d'))
#     df_current=df[df['Date']==dt(2021,12,1)]
#
#     trace1=go.Bar(
#     x='P_A1',
#     y=df_current['P_A1'].astype(int)
#     )
#     trace2=go.Bar(
#     x='P_A2',
#     y=df_current['P_A2'].astype(int)
#     )
#     trace3=go.Bar(
#     x='P_B1',
#     y=df_current['P_B1'].astype(int)
#     )
#     trace4=go.Bar(
#     x='P_B2',
#     y=df_current['P_B2'].astype(int)
#     )
#     trace5=go.Bar(
#     x='P_C1',
#     y=df_current['P_C1'].astype(int)
#     )
#     trace6=go.Bar(
#     x='P_C2',
#     y=df_current['P_C2'].astype(int)
#     )
#
#     trace11=go.Bar(
#     x='A1_p',
#     y=df_current['A1_p'].astype(int)
#     )
#     trace22=go.Bar(
#     x='A2_p',
#     y=df_current['A2_p'].astype(int)
#     )
#     trace33=go.Bar(
#     x='C_B1',
#     y=df_current['C_B1'].astype(int)
#     )
#     trace44=go.Bar(
#     x='C_B2',
#     y=df_current['C_B2'].astype(int)
#     )
#     trace55=go.Bar(
#     x='C_C1',
#     y=df_current['C_C1'].astype(int)
#     )
#     trace66=go.Bar(
#     x='C_C2',
#     y=df_current['C_C2'].astype(int)
#     )
#
#     fig1=go.Figure(data=[trace1, trace2, trace3, trace4, trace5, trace6])
#     fig2=go.Figure(data=[trace11, trace22, trace33, trace44, trace55, trace66])
# elif graph in [4, 5]:
#     df=pd.read_csv('./datasets/CSV/Battery7/shiftwise_temp.csv')
#     df['Date']=df['Date'].apply(lambda x: dt.strptime(x, '%Y-%m-%d'))
#     df_current=df[df['Date']==dt(2021,12,1)]
#
#     trace1=go.Bar(
#     x='P_A1',
#     y=df_current['P_A1'].astype(int)
#     )
#     trace2=go.Bar(
#     x='P_A2',
#     y=df_current['P_A2'].astype(int)
#     )
#     trace3=go.Bar(
#     x='P_B1',
#     y=df_current['P_B1'].astype(int)
#     )
#     trace4=go.Bar(
#     x='P_B2',
#     y=df_current['P_B2'].astype(int)
#     )
#     trace5=go.Bar(
#     x='P_C1',
#     y=df_current['P_C1'].astype(int)
#     )
#     trace6=go.Bar(
#     x='P_C2',
#     y=df_current['P_C2'].astype(int)
#     )
#
#     trace11=go.Bar(
#     x='A1_p',
#     y=df_current['A1_p'].astype(int)
#     )
#     trace22=go.Bar(
#     x='A2_p',
#     y=df_current['A2_p'].astype(int)
#     )
#     trace33=go.Bar(
#     x='C_B1',
#     y=df_current['C_B1'].astype(int)
#     )
#     trace44=go.Bar(
#     x='C_B2',
#     y=df_current['C_B2'].astype(int)
#     )
#     trace55=go.Bar(
#     x='C_C1',
#     y=df_current['C_C1'].astype(int)
#     )
#     trace66=go.Bar(
#     x='C_C2',
#     y=df_current['C_C2'].astype(int)
#     )
#
#     fig1=go.Figure(data=[trace1, trace2, trace3, trace4, trace5, trace6])
#     fig2=go.Figure(data=[trace11, trace22, trace33, trace44, trace55, trace66])
# elif graph in [6, 7]:
#     df=pd.read_csv('./datasets/CSV/Battery8/shiftwise_temp.csv')
#     df['Date']=df['Date'].apply(lambda x: dt.strptime(x, '%Y-%m-%d'))
#     df_current=df[df['Date']==dt(2021,12,1)]
#
#     trace1=go.Bar(
#     x='P_A1',
#     y=df_current['P_A1'].astype(int)
#     )
#     trace2=go.Bar(
#     x='P_A2',
#     y=df_current['P_A2'].astype(int)
#     )
#     trace3=go.Bar(
#     x='P_B1',
#     y=df_current['P_B1'].astype(int)
#     )
#     trace4=go.Bar(
#     x='P_B2',
#     y=df_current['P_B2'].astype(int)
#     )
#     trace5=go.Bar(
#     x='P_C1',
#     y=df_current['P_C1'].astype(int)
#     )
#     trace6=go.Bar(
#     x='P_C2',
#     y=df_current['P_C2'].astype(int)
#     )
#
#     trace11=go.Bar(
#     x='A1_p',
#     y=df_current['A1_p'].astype(int)
#     )
#     trace22=go.Bar(
#     x='A2_p',
#     y=df_current['A2_p'].astype(int)
#     )
#     trace33=go.Bar(
#     x='C_B1',
#     y=df_current['C_B1'].astype(int)
#     )
#     trace44=go.Bar(
#     x='C_B2',
#     y=df_current['C_B2'].astype(int)
#     )
#     trace55=go.Bar(
#     x='C_C1',
#     y=df_current['C_C1'].astype(int)
#     )
#     trace66=go.Bar(
#     x='C_C2',
#     y=df_current['C_C2'].astype(int)
#     )
#
#     fig1=go.Figure(data=[trace1, trace2, trace3, trace4, trace5, trace6])
#     fig2=go.Figure(data=[trace11, trace22, trace33, trace44, trace55, trace66])
#
# return fig1, fig2
# df=pd.read_csv('./datasets/CSV/Battery5/shiftwise_temp.csv')
# df['Date']=df['Date'].apply(lambda x: dt.strptime(x, '%Y-%m-%d'))
# df_current=df[df['Date']==dt(2021,12,1)]

# date=dt.today().strftime('%d-%m-%Y')
# day=int(date.split('-')[0])
#
# try:
#     df_li=[]
#     for jj in tqdm(range(1,day+1), 'compiling daily average temperature...'):
#         #date of sheet_name
#         if len(str(jj))==1:
#             day_sheet='0'+str(jj)
#         else:
#             day_sheet=str(jj)
#         date_sheet='{2}-{1}-{0}'.format(day_sheet, date.split('-')[1], date.split('-')[2])
#
#         df=pd.read_excel(i,engine='openpyxl',sheet_name=str(jj), header=None, usecols=[0,1,2,3,4,5,6,24,25,26,27,28,29], skiprows=[0,1,2])
#         df_avg=df.iloc[[0,74],:]
#         df_avg.fillna(0, inplace=True)
#         df_avg.columns=['Date', 'P_A1', 'P_A2', 'P_B1', 'P_B2', 'P_C1', 'P_C2', 'C_A1', 'C_A2', 'C_B1', 'C_B2', 'C_C1', 'C_C2']
#         df_avg.drop([0], inplace=True)
#
#         #assigning date
#         df_avg.iloc[0,0]=date_sheet
#         df_avg.reset_index(inplace=True, drop=True)
#         df_avg.iloc[:, 1:]=df_avg.iloc[:, 1:].apply(lambda x: int(x))
#         df_li.append(df_avg)
#
#     df_main=pd.concat(df_li, axis=0)
#
#
#         print('compiled',df_main.shape)
#         df_main.to_csv('{}/datasets/CSV/Battery6/shiftwise_temp.csv'.format(os.getcwd()), index=False
#         ,mode="a", header=None
#         )
#         df_main=pd.read_csv('./datasets/CSV/Battery6/shiftwise_temp.csv')
#         df_main.drop_duplicates(subset=['Date'],keep='last',inplace=True)
#         print('final',df_main.shape)
#         df_main.to_csv('{}/datasets/CSV/Battery6/shiftwise_temp.csv'.format(os.getcwd()), index=False)
#
# except Exception as e:
#     print(e)
#     pass

#
# py = pathlib.Path('./datasets/CSV/Schedule').glob("*.csv")
# for source in py:
#     target='/process_data/pushing_rp_backup/Schedule'
#     shutil.copy(source, target)

    #
# def dateswap(x):
#     a=x.split('-')
#     if len(a[-1])==4:
#         a[0],a[2]=a[2],a[0]
#     return '{}-{}-{}'.format(a[0],a[1],a[2])
#
# date=dt.today().replace(hour=0, minute=0, second=0, microsecond=0)- timedelta(days=100)
# fig = make_subplots(rows=2, cols=2, start_cell="top-left")
# row_col=[(1,1),(1,2),(2,2),(2,1)]
#
# for x in range(4):
#     df_p=pd.read_csv('./datasets/CSV/Battery{}/controlps.csv'.format(x+5))
#     df_c=pd.read_csv('./datasets/CSV/Battery{}/controlcs.csv'.format(x+5))
#     df_avg_p=df_p[df_p['oven']=='avg']
#     df_avg_c=df_c[df_c['oven']=='avg']
#
#     df_avg_p['date']=df_avg_p['date'].apply(lambda x: dateswap(x))
#     df_avg_p['date']=df_avg_p['date'].apply(lambda x: dt.strptime(x, '%Y-%m-%d'))
#     df_avg_p=df_avg_p.loc[df_avg_p['date'].between((date-timedelta(days=15)), date)].reset_index(drop=True)
#
#     df_avg_c['date']=df_avg_c['date'].apply(lambda x: dateswap(x))
#     df_avg_c['date']=df_avg_c['date'].apply(lambda x: dt.strptime(x, '%Y-%m-%d'))
#     df_avg_c=df_avg_c.loc[df_avg_c['date'].between((date-timedelta(days=15)), date)].reset_index(drop=True)
#
#     r,c=row_col[x]
#
#     fig.add_trace(
#     go.Scatter(x=df_avg_p['date'], y=df_avg_p['temp']),
#     row=r,col=c
#     )
#     fig.add_trace(
#     go.Scatter(x=df_avg_c['date'], y=df_avg_c['temp']),
#     row=r,col=c
#     )
#
#







# data=[]
# all_df=[]
# for x in range(4):
#     df=pd.read_csv('./datasets/CSV/Battery{}/cokefall.csv'.format(x+5))
#     df['date']=df['date'].apply(lambda x: dateswap(x))
#     df['cokefall_count']=df['value'].apply(lambda x: 1 if x == 'YES' else 0)
#     df_count=df.groupby(['date']).cokefall_count.sum().reset_index()
#
#     df_count['date']=df_count['date'].apply(lambda x: dt.strptime(x, '%Y-%m-%d'))
#     df_count=df_count.loc[df_count['date'].between((date-timedelta(days=15)), date)]
#
#     df_count.rename(columns={'cokefall_count':'cokefall_count{}'.format(x+5)}, inplace=True)
#
#     trace=go.Scatter(
#     x=df_count['date'],
#     y=df_count['cokefall_count{}'.format(x+5)],
#     mode='lines',
#     name='Battery {}'.format(x+5),
#     # fill='tozeroy',
#     line={'shape': 'spline', 'smoothing': 1}
#     )
#
#     all_df.append(df_count)
#     data.append(trace)
#
# df_merged=pd.concat(all_df, axis=1)
# df_merged['total']=df_merged['cokefall_count5']+df_merged['cokefall_count6']+df_merged['cokefall_count7']+df_merged['cokefall_count8']
#
#
# trace_tot=go.Scatter(
# x=df_merged.iloc[:, 0],
# y=df_merged['total'],
# mode='lines',
# name='Total',
# # fill='tozeroy',
# line={'shape': 'spline', 'smoothing': 1}
# )
#
# data.append(trace_tot)
# layout=go.Layout(
# title="Overall Amperage",
#  plot_bgcolor='#FFF',
# xaxis=dict(title='Date', linecolor='#808080', showgrid=False),
# yaxis=dict(title='', linecolor='#808080', showgrid=False),font_size=13,
# showlegend=True
# )
#
# fig=go.Figure(data=data, layout=layout)
# fig.update_layout(hovermode="x unified")

# #
# for x in range(4):
#     df=pd.read_csv('./datasets/CSV/Battery{}/Pushing-report.csv'.format(x+5))
#     df_1=df[['Date', 'Oven No.', 'Amperage', 'Cake Ht.', 'Cokefall', 'Smoke', 'front_side', 'back_side', 'lock_slip']]
#     df_1['Date']=df_1['Date'].apply(lambda x: dateswap(x))
#     df_1['Date']=df_1['Date'].apply(lambda x: dt.strptime(x, '%Y-%m-%d'))
#     # df_1=df_1[df_1['Date'] == date]
#
#     #cokefall DataFrame
#     df_cokefall=df_1.loc[df_1['Cokefall'] == 'YES', ['Oven No.', 'Date', 'Cokefall']]
#     df_cokefall.rename(columns={'Cokefall':'value', 'Date':'date', 'Oven No.':'oven'}, inplace=True)
#     print(df_cokefall)
#
#     #amperage Dataframe
#     df_amperage=df_1.loc[:, ['Oven No.', 'Date', 'Amperage']]
#     df_amperage.rename(columns={'Amperage':'amperage', 'Date':'date', 'Oven No.':'oven'}, inplace=True)
#     df_amperage=df_amperage.loc[df_amperage['amperage']>140]
#     print(df_amperage)


# print(df_1[df_1['Cokefall'] == 'YES'])

# date=dt(2021,8,18)
#
# df=pd.read_csv('./datasets/CSV/TE Data/DM Data_blend.csv',header=2)
# df_blend=df[['Unnamed: 0', 'Blend', 'Blend.1']]
# df_blend.rename(columns={'Unnamed: 0':'date', 'Blend':'co3', 'Blend.1':'co4'}, inplace=True)
# df_blend.dropna(inplace=True)
# df_blend['date']=df_blend['date'].apply(lambda x: dt.strptime(x, '%d-%b-%y'))
# #filtering by date
# df_blend=df_blend.loc[df_blend['date']==date, :].reset_index(drop=True)
# if not(df_blend.empty):
#     blend_value=[]
#     for i in range(len(df_blend.co3[0].split(','))):
#         blend_percentage=df_blend.co3[0].split(',')[i].split('-')
#         if len(blend_percentage)==2:
#             blend_percentage=df_blend.co3[0].split(',')[i].split('-')[-1][:-1]
#         elif len(blend_percentage)==3:
#             blend_percentage=df_blend.co3[0].split(',')[i].split('-')[1][:-1]
#         try:
#             blend_value.append(int(blend_percentage))
#         except:
#             pass
#     blend_label=df_blend.co3[0].split(',')


# df_1=pd.read_csv('./datasets/CSV/TE Data/DM Data.csv',header=2,parse_dates=['Month'])
# df_1.rename(columns={'CO #3.5':' CO3_sp_power',
#                      'CO #4.5':' CO4_sp_power',
#                      'CO #3.6':' CO3_sp_steam',
#                      'CO #4.6':' CO4_sp_steam',
#                      'CO #3.7':' CO3_sp_gas',
#                      'CO #4.7':' CO4_sp_gas',
#                      'CO #3.8':' CO3_sp_tar',
#                      'CO #4.8':' CO4_sp_tar'
#                         }, inplace=True)
# # df_1=df_1[['Month', '3 Pushings', '4 Pushings', ]]
#
# print(df_1.columns)

# print(df_1['CO #3.6'])


# print(df.info())
# df.dropna(subset=['Act. Charging(Time)'], inplace=True)
# for i,v in df['Act. Charging(Time)'].iteritems():
#     if '.' in v:
#         print(df.loc[i, 'Oven No.'])
# df_wrong_charging_time=df.loc[df['Act. Charging(Time)'].str.contains('.')]\

#
# def dateswap(x):
#     a=x.split('-')
#     if len(a[0])==4:
#         a[0],a[2]=a[2],a[0]
#     return '{}-{}-{}'.format(a[0],a[1],a[2])
# def series(oven,s):
#     l=[]
#     for i in range(9):
#         l.append(oven)
#         u=int(oven%10)
#         t=int((oven/10)%10)
#
#         for i in range(7-t):
#             oven=oven+10
#             l.append(oven)
#             if len(l)>=s:
#                 break
#
#         if u==9:
#             oven=int(oven/100)*100+(2)
#         elif u==8:
#             oven=int(oven/100)*100+(1)
#         else:
#             oven=int(oven/100)*100+(u+2)
#
#         if len(l)>=s:
#             break
#     return l
#
#
# oven_li_all_battery=[]
# for x in range(5,9):
#     df=pd.read_csv('./datasets/CSV/Battery{}/Pushing-report.csv'.format(x))
#     df['Date']=df['Date'].apply(lambda x: dateswap(x))
#     df['Date']=df['Date'].apply(lambda x: dt.strptime(x,'%d-%m-%Y'))
#
#     # a=dt.strptime(str(dt.date(dt.today())), '%Y-%m-%d')
#     a=dt(2021,10,25)
#     present_day_oven=df.loc[df['Date']==a, 'Oven No.'].astype(int).tolist()
#
#     oven_li_all_battery.append(present_day_oven)
#
# all_oven_series_5=series(501,72)
# all_oven_series_6=series(601,72)
# all_oven_series_7=series(701,72)
# all_oven_series_8=series(801,72)
# all_oven_series_li=[all_oven_series_5, all_oven_series_6, all_oven_series_7, all_oven_series_8]
#
# li_z_all=[]
# li_z_text_all=[]
#
# oven_li_all_battery[3]=oven_li_all_battery[3]+[878]
#
# for xx in range(4):
#     li=[(1.0,i) if i in oven_li_all_battery[xx] else (0,i)  for i in all_oven_series_li[xx]]
#     #list of oven present multiple times
#     li_dup=[i  for i in oven_li_all_battery[xx] if oven_li_all_battery[xx].count(i)>1]
#
#     z=[]
#     x=[]
#     for i in li:
#         a,b=i
#         z.append(a)
#         x.append(b)
#
#     if li_dup != []:
#         for ii in li_dup:
#             z[x.index(ii)]=0.5
#
#     li_z_all.append(z)
#     li_z_text_all.append(x)
#
# z_all_li=[]
# z_all__text_li=[]
#
#
# for xx in range(4):
#     z_c=li_z_all[xx]
#     z_c=[z_c[0:18], z_c[18:36], z_c[36:54], z_c[54:72]]
#
#     z_c_text=li_z_text_all[xx]
#     z_c_text=[z_c_text[0:18], z_c_text[18:36], z_c_text[36:54], z_c_text[54:72]]
#
#     z_all_li.append(z_c)
#     z_all__text_li.append(z_c_text)
#
#
#
# colorscale=[[0, 'rgb(255,255,255)'], [0.5, '#f9ff4d'], [1, '#33a532']]
# # font_colors = ['black', 'orange', 'white']
# font_colors = ['black']
#
# #all battery figures
# figures_li=[]
#
# for xxx in range(4):
#     fig = ff.create_annotated_heatmap(z=z_all_li[xxx], annotation_text=z_all__text_li[xxx],
#     colorscale=colorscale, font_colors=font_colors)
#     figures_li.append(fig)
#
# # fig = make_subplots(rows=2, cols=2, start_cell="top-left")
# # row_col=[(1,1),(1,2),(2,2),(2,1)]
#
# # ann=[]
# # for xx in range(4):
# #
# #     r,c=row_col[xx]
# #     fig1 = ff.create_annotated_heatmap(z=z_all_li[xx], annotation_text=z_all__text_li[xx], colorscale=colorscale)
# #
# #     fig.add_trace(
#     fig1.data[0],
#     row=r,col=c
#     # layout=go.Layout(yaxis={'visible':False})
#     )
#     ann_li=list(fig1.layout.annotations)
#
#     for k  in range(len(ann_li)):
#         ann_li[k]['xref'] = 'x{}'.format(xx+1)
#         ann_li[k]['yref'] = 'y{}'.format(xx+2)
#
#     ann.append(ann_li)


    # figures.append(fig)
    # fig.update_layout(showlegend=False)
    # fig = ff.create_annotated_heatmap(z=z_all_li[xx], annotation_text=z_all__text_li[xx], colorscale=colorscale)

# annot1 = list(fig1.layout.annotations)
# annot2 = list(fig2.layout.annotations)
# for k  in range(len(annot2)):
#     annot2[k]['xref'] = 'x2'
#     annot2[k]['yref'] = 'y2'
# fig.update_layout(annotations=ann[0]+ann[1]+ann[2]+ann[3])



# print(colorscale)
# fig = ff.create_annotated_heatmap(z=z_all_li[3], annotation_text=z_all__text_li[3], colorscale=colorscale)
# fig.show()

# print(z_all_li[xx])
# print(type(z_all_li[xx][0][0]))
# '''-----Functions------'''
# def series(oven,s):
#     l=[]
#     for i in range(9):
#         l.append(oven)
#         u=int(oven%10)
#         t=int((oven/10)%10)
#
#         for i in range(7-t):
#             oven=oven+10
#             l.append(oven)
#             if len(l)>=s:
#                 break
#
#         if u==9:
#             oven=int(oven/100)*100+(2)
#         elif u==8:
#             oven=int(oven/100)*100+(1)
#         else:
#             oven=int(oven/100)*100+(u+2)
#
#         if len(l)>=s:
#             break
#     return l
#
# def timedelta_to_string(cpd):
#     days=cpd.days
#     seconds=cpd.seconds
#     hours = seconds//3600
#     minutes = (seconds//60)%60
#     if days>=1:
#         hours=hours+days*24
#     if minutes<10:
#         return '{}:0{}'.format(hours,minutes)
#     else:
#         return '{}:{}'.format(hours,minutes)
#
# def timedelta_fromdict(d):
#     for i,j in d.items():
#         hours,minutes,seconds=j.split(':')
#         d[i]=timedelta(hours=int(hours),minutes=int(minutes))
#     return d
#
# def timedelta_fromstring(s):
#         hours,minutes=s.split(':')
#         t=timedelta(hours=int(hours),minutes=int(minutes))
#         return t
#
# def comparison(sch,cpd):
#     if sch>=cpd:
#         return sch
#     elif sch<cpd:
#         return cpd
# def adding_cpd(oven,charging_time,ovens_cpd):
#     cpd_hours=ovens_cpd[oven]
#     charging_time=charging_time+cpd_hours
#     return charging_time
# #parsing Functions
# def numeric_to_datetime(start,stop, shift):
#
#     if (shift=='A')|((shift=='B')):
#         if start == None:
#             start=dt(2021,1,1)
#         elif start != None:
#
#             time=dt.time(dt.strptime(start,'%H:%M'))
#             date=dt.date(dt.today())
#             start=dt.combine(date,time)
#
#         if stop == None:
#             stop=dt(2021,1,1)
#         elif stop != None:
#             time=dt.time(dt.strptime(stop,'%H:%M'))
#             date=dt.date(dt.today())
#             stop=dt.combine(date,time)
#
#     elif shift=='C':
#
#         if start == None:
#             start=dt(2021,1,1)
#         elif start != None:
#
#             time=dt.time(dt.strptime(start,'%H:%M'))
#             if (time>=dt.time(dt(2021,1,1,22,0)))&(time<=dt.time(dt(2021,1,1,23,59))):
#                 date=dt.date(dt.today())
#                 start=dt.combine(date,time)
#             else:
#                 date=dt.date(dt.today()+timedelta(day=1))
#                 start=dt.combine(date,time)
#
#         if stop == None:
#             stop=dt(2021,1,1)
#         elif stop != None:
#
#             time=dt.time(dt.strptime(stop,'%H:%M'))
#             if (time>=dt.time(dt(2021,1,1,22,0)))&(time<=dt.time(dt(2021,1,1,23,59))):
#                 date=dt.date(dt.today())
#                 stop=dt.combine(date,time)
#             else:
#                 date=dt.date(dt.today()+timedelta(day=1))
#                 stop=dt.combine(date,time)
#     return start,stop
#
#
# # #to find missing ovens
# # def find_ofs(battery,list_oven_sch):
# #
# #     df_missing=pd.DataFrame(list_oven_sch, columns=['Oven'])
# #     df_missing['series']=df_missing['Oven']
#
# #to find missing ovens
# def find_missing_ovens(battery,list_oven_sch):
#
#     if int(battery) == 5:
#         df_main=pd.DataFrame(series(501,72), columns=['Ovens_main'])
#
#     elif int(battery) == 6:
#         df_main=pd.DataFrame(series(601,72), columns=['Ovens_main'])
#
#     elif int(battery) == 7:
#         df_main=pd.DataFrame(series(701,72), columns=['Ovens_main'])
#
#     elif int(battery) == 8:
#         df_main=pd.DataFrame(series(801,72), columns=['Ovens_main'])
#
#     df_main['series']=df_main['Ovens_main'].apply(lambda x: int(x)%10)
#
#     df_missing=pd.DataFrame(list_oven_sch, columns=['Oven'])
#     df_missing['series']=df_missing['Oven'].apply(lambda x: int(x)%10)
#     df_missing['series_count']=df_missing.groupby('series')['Oven'].transform('count')
#     df_missing=df_missing[df_missing['series_count']>5]
#
#
#     series_li=df_missing['series'].unique().tolist()
#
#     # #To not consider starting & last series
#     # del series_li[0]
#     # del series_li[-1]
#
#     missing_ovens_final_li=[]
#
#     for s in series_li:
#
#         #ovens in schedule
#         oven_sch_li=df_missing.loc[df_missing['series']==s,'Oven'].tolist()
#         oven_sch=np.array(oven_sch_li)
#
#         #ovens in original series
#         oven_og_li=df_main.loc[df_main['series']==s,'Ovens_main'].tolist()
#         oven_og=np.array(oven_og_li)
#
#         #getting missing ovens
#         #elememt wise reversal of boolean values
#         li=np.invert(np.array([(i in oven_sch) for i in oven_og]))
#
#         missing_ovens_final=oven_og[li].tolist()
#         missing_ovens_final1=missing_ovens_final.copy()
#         for o in missing_ovens_final1 :
#             if o != oven_og_li[-1]:
#                 # print(oven_og_li[oven_og_li.index(o)-1])
#                 if oven_og_li[oven_og_li.index(o)+1]==oven_sch_li[0]:
#                     print(1,o)
#                     del missing_ovens_final[missing_ovens_final.index(o)]
#                 if oven_og_li[oven_og_li.index(o)-1]==oven_sch_li[-1]:
#                     print(2,o)
#                     del missing_ovens_final[missing_ovens_final.index(o)]
#             elif o == oven_og_li[-1]:
#                 del missing_ovens_final[missing_ovens_final.index(o)]
#         missing_ovens_final_li.extend(missing_ovens_final)
#     return missing_ovens_final_li
#
#
#
# a=find_missing_ovens(5,[521,531,541,551,561,571])
# print(a)
#519,529,539,549,559,569
# #to find OFS ovens
# def find_ofs(battery,list_oven_sch):
#
#     if int(battery)==5:
#         a=series(501,72)
#     elif int(battery)==6:
#         a=series(601,72)
#     elif int(battery)==7:
#         a=series(701,72)
#     elif int(battery)==8:
#         a=series(801,72)
#     else:
#         return None
#
#     #first & last ovn of unit_series
#     first_oven_series=a[0]
#     last_oven_series=a[-1]
#
#     list_oven_sch=[int(i) for i in list_oven_sch]
#
#     all_ofs=[]
#
#     for i in list_oven_sch:
#
#         if list_oven_sch.index(i) ==0:
#             if i==first_oven_series:
#                 prev_oven_actual=a[a.index(i)+2]
#                 next_oven_actual=a[a.index(i)+1]
#                 all_three_actual=np.array([prev_oven_actual,i,next_oven_actual])
#
#                 prev_oven_current=list_oven_sch[list_oven_sch.index(i)+2]
#                 next_oven_current=list_oven_sch[list_oven_sch.index(i)+1]
#                 all_three_current=np.array([i,next_oven_current,prev_oven_current])
#                 result=(all_three_actual==all_three_current).sum()
#                 if result <2:
#
#                     all_ofs.append(i)
#             elif i==last_oven_series:
#                 prev_oven_actual=a[0]
#                 next_oven_actual=a[1]
#                 all_three_actual=np.array([i,prev_oven_actual,next_oven_actual])
#
#                 prev_oven_current=list_oven_sch[list_oven_sch.index(i)+1]
#                 next_oven_current=list_oven_sch[list_oven_sch.index(i)+2]
#                 all_three_current=np.array([i,prev_oven_current,next_oven_current])
#
#                 result=(all_three_actual==all_three_current).sum()
#                 if result <2:
#
#                     all_ofs.append(i)
#
#             else:
#                 prev_oven_actual=a[a.index(i)-1]
#                 next_oven_actual=a[a.index(i)+1]
#                 all_three_actual=np.array([prev_oven_actual,i,next_oven_actual])
#
#                 prev_oven_current=list_oven_sch[list_oven_sch.index(i)-1]
#                 next_oven_current=list_oven_sch[list_oven_sch.index(i)+1]
#                 all_three_current=np.array([prev_oven_current,i,next_oven_current])
#                 result=(all_three_actual==all_three_current).sum()
#                 if result <2:
#
#                     all_ofs.append(i)
#         elif list_oven_sch.index(i)==len(list_oven_sch)-1:
#             if i==first_oven_series:
#                 prev_oven_actual=a[-1]
#                 next_oven_actual=a[-2]
#                 all_three_actual=np.array([next_oven_actual,prev_oven_actual,i])
#
#                 prev_oven_current=list_oven_sch[list_oven_sch.index(i)-2]
#                 next_oven_current=list_oven_sch[list_oven_sch.index(i)-1]
#                 all_three_current=np.array([prev_oven_current,next_oven_current,i])
#                 result=(all_three_actual==all_three_current).sum()
#                 if result <2:
#
#                     all_ofs.append(i)
#             elif i==last_oven_series:
#                 prev_oven_actual=a[a.index(i)-2]
#                 next_oven_actual=a[a.index(i)-1]
#                 all_three_actual=np.array([prev_oven_actual,next_oven_actual,i])
#
#                 prev_oven_current=list_oven_sch[list_oven_sch.index(i)-2]
#                 next_oven_current=list_oven_sch[list_oven_sch.index(i)-1]
#                 all_three_current=np.array([prev_oven_current,next_oven_current,i])
#                 result=(all_three_actual==all_three_current).sum()
#                 if result <2:
#
#                     all_ofs.append(i)
#             else:
#                 prev_oven_actual=a[a.index(i)-2]
#                 next_oven_actual=a[a.index(i)-1]
#                 all_three_actual=np.array([prev_oven_actual,next_oven_actual,i])
#
#                 prev_oven_current=list_oven_sch[list_oven_sch.index(i)-2]
#                 next_oven_current=list_oven_sch[list_oven_sch.index(i)-1]
#                 all_three_current=np.array([prev_oven_current,next_oven_current,i])
#                 result=(all_three_actual==all_three_current).sum()
#                 if result <2:
#
#                     all_ofs.append(i)
#
#         else:
#             try:
#                 if i==first_oven_series:
#                     prev_oven_actual=a[-1]
#                     next_oven_actual=a[a.index(i)+1]
#                     all_three_actual=np.array([prev_oven_actual,i,next_oven_actual])
#
#                     prev_oven_current=list_oven_sch[list_oven_sch.index(i)-1]
#                     next_oven_current=list_oven_sch[list_oven_sch.index(i)+1]
#                     all_three_current=np.array([prev_oven_current,i,next_oven_current])
#
#                     result=(all_three_actual==all_three_current).sum()
#
#
#                     if result <2:
#                         all_ofs.append(i)
#                 elif i==last_oven_series:
#                     prev_oven_actual=a[a.index(i)-1]
#                     next_oven_actual=a[0]
#                     all_three_actual=np.array([prev_oven_actual,i,next_oven_actual])
#
#                     prev_oven_current=list_oven_sch[list_oven_sch.index(i)-1]
#                     next_oven_current=list_oven_sch[list_oven_sch.index(i)+1]
#                     all_three_current=np.array([prev_oven_current,i,next_oven_current])
#
#                     result=(all_three_actual==all_three_current).sum()
#
#
#                     if result <2:
#                         all_ofs.append(i)
#                 else:
#                     prev_oven_actual=a[a.index(i)-1]
#                     next_oven_actual=a[a.index(i)+1]
#                     all_three_actual=np.array([prev_oven_actual,i,next_oven_actual])
#
#                     prev_oven_current=list_oven_sch[list_oven_sch.index(i)-1]
#                     next_oven_current=list_oven_sch[list_oven_sch.index(i)+1]
#                     all_three_current=np.array([prev_oven_current,i,next_oven_current])
#
#                     result=(all_three_actual==all_three_current).sum()
#
#
#                     if result <2:
#                         all_ofs.append(i)
#
#             except Exception as e:
#                 print(e,i)
#                 pass
#
#     return all_ofs
#
# #to check against any matching timings between two batteries
# def match_timing_check(l1,l2):
#     '''
#     l1 & l2 are list of timings in both batteries.
#     Returns updated list of timing for 2nd battery & string for verification!
#     '''
#     s_output=''
#     for time_1 in l1:
#         for time_2 in l2:
#             if time_1==time_2:
#                 s_output=s_output+'1'
#                 # index of matched time
#                 index_match=l2.index(time_2)
#
#                 if index_match!=0:
#                     time_2_prev=l2[index_match-1]
#                     if (time_2-time_2_prev)>timedelta(minutes=15):
#                         time_2=(time_2-timedelta(minutes=5))
#                     else:
#                         time_2=(time_2+timedelta(minutes=5))
#                 else:
#                     time_2=(time_2+timedelta(minutes=5))
#
#                 l2[index_match]=time_2
#     return (l2, s_output)
# def shutdown_gap(S,stoppages,mpp):
#
#     '''
#     S- Series containing the time column of DataFrame
#     stoppage- List of tuples containing start & stop timing (Count=3)
#     mpp- minutes per pushing
#     '''
#
#     if mpp<15:
#         mpp=15
#     stoppage=stoppages
#     xx=[]
#     min=[]
#
#     df=S
#     df1=S
#     d=None
#     a=None
#
#     for j in range(3):
#
#         x,y=stoppage[j]
#
#
#         if (x-y)!=timedelta(minutes=0):
#             index=1
#             ss='No oven in stoppage'
#             for i,value in df1.items():
#
#                 h=value
#
#                 if (h>x)&(h<y):
#                     index=i
#                     ss='Oven in stoppage'
#
#                     # print(h)
#                     # if (x-df1.loc[i-1])>=timedelta(minutes=15):
#                     #     df1.loc[i]=x
#                     #     index=i+1
#                     #     if j==2:
#                     #         break
#                     #     else:
#                     #         continue
#                     # else:
#                     gap=y-h
#                     break
#                 else:
#                     continue
#             if ss=='Oven in stoppage':
#                 if (j==0):
#                     a=df.loc[:index-1]
#                     d=index
#
#
#                 timings=df1.loc[index:].tolist()
#
#                 t=y
#                 h=[y]
#                 minute=[(y.strftime('%H'),y.strftime('%M'))]
#                 for i in range(len(timings)-1):
#                     t=t+timedelta(minutes=mpp)
#                     h.append(t)
#
#                     minutes=t.strftime('%M')
#                     hours=t.strftime('%H')
#                     minute.append((hours,minutes))
#                 min.extend(minute)
#
#                 df.loc[index:]=h
#                 df1=df.loc[index:]
#         else:
#             continue
#     if d!=None:
#         df.loc[:d-1]=a.tolist()
#
#     minute=df.apply(lambda x: (x.hour,x.minute)).tolist()
#
#     Time_schd=[]
#     for i in minute:
#         hr,m=i
#         u=int(m)%10
#         if u<=5:
#             diff=5-u
#             if diff>=3:
#                 min=int(m)-u
#             else:
#                 min=int(m)+diff
#         elif u>5:
#             diff=10-u
#             if diff>=3:
#                 min=int(m)-(5-diff)
#             else:
#                 min=int(m)+diff
#         if min>=55:
#             min=55
#         if len(str(min))==1:
#             min='0'+str(min)
#         time=str(hr)+':'+str(min)
#
#         Time_schd.append(dt.strptime(time,'%H:%M').time())
#     date_li=df.apply(lambda x: dt.date(x))
#     a=zip(date_li,Time_schd)
#     final_time=[]
#
#     for i,j in a:
#         time=dt.combine(i,j)
#         final_time.append(time)
#
#     df=final_time
#
#     return df
#
# def min_cpd_checker(df,min_cpd):
#
#     df['Final']=df.apply(lambda row: row['Final']+(min_cpd-row['CPD']) if row['CPD']<min_cpd else row['Final'],axis=1)
#     df['CPD']=df['CPD'].apply(lambda x: min_cpd if x<min_cpd else x)
#
#
#     return df
#
# def min_gap_btw_ovens(timings):
#     '''
#     timings is a list.
#     Returns datetime list of datetime object if input is date time & return string datetime if input is string.
#     output_format- To check if input in string format
#     output_str-To output string for verification
#
#     '''
#
#     for i in range(len(timings)):
#
#         output_format='no'
#         output_str=''
#         if (i != 0)&(timings[i]!=None):
#
#             if type(timings[i])==type('s'):
#                 output_format='yes'
#                 current_time=dt.strptime(timings[i],'%H:%M')
#             else:
#                 current_time=timings[i]
#             if type(timings[i-1])==type('s'):
#                 prev_time=dt.strptime(timings[i-1],'%H:%M')
#             else:
#                 prev_time=timings[i-1]
#
#
#             gap=current_time-prev_time
#             if gap<timedelta(minutes=15):
#                 output_str='1'
#                 current_time=current_time+timedelta(minutes=5)
#
#             if output_format=='yes':
#                 timings[i]=current_time.strftime('%H:%M')
#             else:
#                 timings[i]=current_time
#
#     return (timings, output_str)
#
# def pph(df,battery):
#
#     #pushing per hour
#     df['Pushing{}'.format(battery)]=df['Pushing{}'.format(battery)].apply(lambda x: dt.strptime(x,'%Y-%m-%dT%H:%M:%S'))
#     df['hour']=df['Pushing{}'.format(battery)].dt.hour
#     df['PPH{}'.format(battery)]=df.groupby('hour')['Final{}'.format(battery)].transform('count')
#     df['PPH{}'.format(battery)]=df.apply(lambda row: '( ' + str(row['hour']) + ' , ' +  str(row['PPH{}'.format(battery)]) + ' )', axis=1)
#     df.drop('hour',axis=1,inplace=True)
#
#     return df
#
#
# df=pd.read_csv('./datasets/CSV/Battery6/Pushing-report.csv').tail(500)
# df.dropna(subset=['Act. Charging(Time)'], inplace=True)
# df['Date']=df['Date'].apply(lambda x:dt.strptime(x,'%m/%d/%y') if '/' in x else dt.strptime(x,'%Y-%m-%d'))
# df['Act. Charging(Time)']=df['Act. Charging(Time)'].apply(lambda x: timedelta_fromstring(x[:-3]))
# df['Prev day charging time']=df['Act. Charging(Time)'] + df['Date']
# df['Prev day charging time']=df.apply(lambda row:row['Prev day charging time']+timedelta(days=1) if (row['Shift']=='C1')&(row['Prev day charging time'].time()>=dt(21,1,1,0,0).time())&(row['Prev day charging time'].time()<=dt(21,1,1,7,0).time()) else row['Prev day charging time'], axis=1)
# df['Prev day charging time']=df.apply(lambda row:row['Prev day charging time']-timedelta(days=1) if (row['Shift']=='C2')&(row['Prev day charging time'].time()>=dt(21,1,1,22,0).time())&(row['Prev day charging time'].time()<=dt(21,1,1,23,59).time()) else row['Prev day charging time'], axis=1)
# df['Charging time']=df.groupby('Oven No.')['Prev day charging time'].transform('max')
# df_new=df[df['Charging time']==df['Prev day charging time']].sort_values('Prev day charging time',ascending=True).reset_index()
#
#
# # df_next_avail['Act. Charging(Time)']=df_next_avail['Act. Charging(Time)'].apply(timedelta_to_string)
# # df_next_avail['Act. Charging(Time)']=df_next_avail['Act. Charging(Time)'].apply(lambda x : (dt.strptime(x,'%H:%M')).strftime('%H:%M'))
# # df_next_avail=df_next_avail[['Oven No.','Act. Charging(Time)','Cake Ht.','Prev day charging time']]
# # df_next_avail.columns=['Oven No.','Charging(Time)','Cake Ht.','Charging_time_datetime']
# print(df_new[df_new['Oven No.']==605])
# #
# def series(oven,s):
#     l=[]
#     for i in range(9):
#         l.append(oven)
#         u=int(oven%10)
#         t=int((oven/10)%10)
#
#         for i in range(7-t):
#             oven=oven+10
#             l.append(oven)
#             if len(l)>=s:
#                 break
#
#         if u==9:
#             oven=int(oven/100)*100+(2)
#         elif u==8:
#             oven=int(oven/100)*100+(1)
#         else:
#             oven=int(oven/100)*100+(u+2)
#
#         if len(l)>=s:
#             break
#     return l
#
#
#
#
# #to find missing ovens
# def find_missing_ovens(battery,list_oven_sch):
#
#
#
#     if int(battery) == 5:
#         df_main=pd.DataFrame(series(501,72), columns=['Ovens_main'])
#
#     elif int(battery) == 6:
#         df_main=pd.DataFrame(series(601,72), columns=['Ovens_main'])
#
#     elif int(battery) == 7:
#         df_main=pd.DataFrame(series(701,72), columns=['Ovens_main'])
#
#     elif int(battery) == 8:
#         df_main=pd.DataFrame(series(801,72), columns=['Ovens_main'])
#
#     df_main['series']=df_main['Ovens_main'].apply(lambda x: int(x)%10)
#
#     df_missing=pd.DataFrame(list_oven_sch, columns=['Oven'])
#     df_missing['series']=df_missing['Oven'].apply(lambda x: int(x)%10)
#
#     series_li=df_missing['series'].unique().tolist()
#
#     missing_ovens_final_li=[]
#
#     for s in series_li:
#
#         #ovens in schedule
#         oven_sch=np.array(df_missing.loc[df_missing['series']==s,'Oven'].tolist())
#
#         #ovens in original series
#         oven_og=np.array(df_main.loc[df_main['series']==s,'Ovens_main'].tolist())
#
#         #getting missing ovens
#         #elememt wise reversal of boolean values
#         li=np.invert(np.array([(i in oven_sch) for i in oven_og]))
#
#         missing_ovens_final=oven_og[li]
#
#         missing_ovens_final_li.extend(missing_ovens_final)
#     return missing_ovens_final_li
#
# oven=[521,511,531,541,561,555,546,544]
#
#
#
# find_missing_ovens(5, oven)
# # df1=pd.read_csv('tst.csv')
# #
# # b_li1=[5,7]
# # b_li2=[6,8]
# #
# # #DataFrames
# # df_li=[df1,df2]
# #
# # for x in range(2):
# #
# #     df1=df_li[x]
# #
# #     # df1['Pushing{}'.format(b_li1[x])]=df1['Pushing{}'.format(b_li1[x])].apply(lambda x: dt.strptime(x,'%Y-%m-%d %H:%M:%S'))
# #     # df1['Pushing{}'.format(b_li2[x])]=df1['Pushing{}'.format(b_li2[x])].apply(lambda x: dt.strptime(x,'%Y-%m-%d %H:%M:%S'))
# #
# #
# #     df5_sync=df1[df1['Oven No.{}'.format(b_li1[x])]!=' '].copy()
# #     df6_sync=df1[df1['Oven No.{}'.format(b_li2[x])]!=' '].copy()
# #
# #
# #     df5_sync['hour']=df5_sync['PPH{}'.format(b_li1[x])].apply(lambda x: int(x.split(' ')[1]) )
# #     df6_sync['hour']=df6_sync['PPH{}'.format(b_li2[x])].apply(lambda x: int(x.split(' ')[1]) )
# #
# #     pph5=df5_sync['PPH{}'.format(b_li1[x])].unique().tolist()
# #     pph6=df6_sync['PPH{}'.format(b_li2[x])].unique().tolist()
# #
# #
# #     p5={}
# #     p6={}
# #     pph=[pph5,pph6]
# #     p=[p5,p6]
# #     hours_li=[i for i in range(14,22)]
# #     hour_5=[]
# #     hour_6=[]
# #     hour_bat=[hour_5,hour_6]
# #     hnp5=[]
# #     hnp6=[]
# #     hour_not_present=[hnp5,hnp6]
# #     for i in range(2):
# #         for j in pph[i]:
# #             h=int(j.split(' ')[1])
# #             n=int(j.split(' ')[3])
# #             # if h!=15:
# #             p[i][h]=n
# #             hour_bat[i].append(h)
# #
# #         for j in hours_li:
# #             if j not in hour_bat[i]:
# #                 p[i][j]=0
# #
# #
# #     df6_sync_copy=df6_sync.loc[df6_sync['hour']==15].reset_index(drop=True)
# #
# #     for hour in hours_li:
# #         #number of pushing
# #         n5=p5[hour]
# #         n6=p6[hour]
# #
# #         if n5==n6:
# #             if n5==3:
# #                 df5_sync_copy=df5_sync.loc[df5_sync['hour']==hour].reset_index(drop=True)
# #                 df5_sync_copy.loc[0,'Pushing{}'.format(b_li1[x])]=df5_sync_copy.loc[0,'Pushing{}'.format(b_li1[x])].replace(minute=10)
# #                 df5_sync_copy.loc[1,'Pushing{}'.format(b_li1[x])]=df5_sync_copy.loc[1,'Pushing{}'.format(b_li1[x])].replace(minute=30)
# #                 df5_sync_copy.loc[2,'Pushing{}'.format(b_li1[x])]=df5_sync_copy.loc[2,'Pushing{}'.format(b_li1[x])].replace(minute=50)
# #                 df5_sync.loc[df5_sync['hour']==hour, 'Pushing{}'.format(b_li1[x])]=df5_sync_copy['Pushing{}'.format(b_li1[x])].tolist()
# #
# #                 df6_sync_copy=df6_sync[df6_sync['hour']==hour].reset_index(drop=True)
# #                 df6_sync_copy.loc[0,'Pushing{}'.format(b_li2[x])]=df6_sync_copy.loc[0,'Pushing{}'.format(b_li2[x])].replace(minute=15)
# #                 df6_sync_copy.loc[1,'Pushing{}'.format(b_li2[x])]=df6_sync_copy.loc[1,'Pushing{}'.format(b_li2[x])].replace(minute=35)
# #                 df6_sync_copy.loc[2,'Pushing{}'.format(b_li2[x])]=df6_sync_copy.loc[2,'Pushing{}'.format(b_li2[x])].replace(minute=55)
# #                 df6_sync.loc[df6_sync['hour']==hour, 'Pushing{}'.format(b_li2[x])]=df6_sync_copy['Pushing{}'.format(b_li2[x])].tolist()
# #
# #             elif n5==4:
# #                 df5_sync_copy=df5_sync[df5_sync['hour']==hour].reset_index(drop=True)
# #                 df5_sync_copy.loc[0,'Pushing{}'.format(b_li1[x])]=df5_sync_copy.loc[0,'Pushing{}'.format(b_li1[x])].replace(minute=5)
# #                 df5_sync_copy.loc[1,'Pushing{}'.format(b_li1[x])]=df5_sync_copy.loc[1,'Pushing{}'.format(b_li1[x])].replace(minute=20)
# #                 df5_sync_copy.loc[2,'Pushing{}'.format(b_li1[x])]=df5_sync_copy.loc[2,'Pushing{}'.format(b_li1[x])].replace(minute=35)
# #                 df5_sync_copy.loc[3,'Pushing{}'.format(b_li1[x])]=df5_sync_copy.loc[3,'Pushing{}'.format(b_li1[x])].replace(minute=50)
# #                 df5_sync.loc[df5_sync['hour']==hour, 'Pushing{}'.format(b_li1[x])]=df5_sync_copy['Pushing{}'.format(b_li1[x])].tolist()
# #
# #                 df6_sync_copy=df6_sync[df6_sync['hour']==hour].reset_index(drop=True)
# #                 df6_sync_copy.loc[0,'Pushing{}'.format(b_li2[x])]=df6_sync_copy.loc[0,'Pushing{}'.format(b_li2[x])].replace(minute=10)
# #                 df6_sync_copy.loc[1,'Pushing{}'.format(b_li2[x])]=df6_sync_copy.loc[1,'Pushing{}'.format(b_li2[x])].replace(minute=25)
# #                 df6_sync_copy.loc[2,'Pushing{}'.format(b_li2[x])]=df6_sync_copy.loc[2,'Pushing{}'.format(b_li2[x])].replace(minute=40)
# #                 df6_sync_copy.loc[3,'Pushing{}'.format(b_li2[x])]=df6_sync_copy.loc[3,'Pushing{}'.format(b_li2[x])].replace(minute=55)
# #                 df6_sync.loc[df6_sync['hour']==hour, 'Pushing{}'.format(b_li2[x])]=df6_sync_copy['Pushing{}'.format(b_li2[x])].tolist()
# #
# #
# #         elif n5!=n6:
# #             if n5==3:
# #                 df5_sync_copy=df5_sync[df5_sync['hour']==hour].reset_index(drop=True)
# #                 df5_sync_copy.loc[0,'Pushing{}'.format(b_li1[x])]=df5_sync_copy.loc[0,'Pushing{}'.format(b_li1[x])].replace(minute=10)
# #                 df5_sync_copy.loc[1,'Pushing{}'.format(b_li1[x])]=df5_sync_copy.loc[1,'Pushing{}'.format(b_li1[x])].replace(minute=30)
# #                 df5_sync_copy.loc[2,'Pushing{}'.format(b_li1[x])]=df5_sync_copy.loc[2,'Pushing{}'.format(b_li1[x])].replace(minute=50)
# #                 df5_sync.loc[df5_sync['hour']==hour, 'Pushing{}'.format(b_li1[x])]=df5_sync_copy['Pushing{}'.format(b_li1[x])].tolist()
# #             elif n5==4:
# #                 df5_sync_copy=df5_sync[df5_sync['hour']==hour].reset_index(drop=True)
# #                 df5_sync_copy.loc[0,'Pushing{}'.format(b_li1[x])]=df5_sync_copy.loc[0,'Pushing{}'.format(b_li1[x])].replace(minute=5)
# #                 df5_sync_copy.loc[1,'Pushing{}'.format(b_li1[x])]=df5_sync_copy.loc[1,'Pushing{}'.format(b_li1[x])].replace(minute=20)
# #                 df5_sync_copy.loc[2,'Pushing{}'.format(b_li1[x])]=df5_sync_copy.loc[2,'Pushing{}'.format(b_li1[x])].replace(minute=35)
# #                 df5_sync_copy.loc[3,'Pushing{}'.format(b_li1[x])]=df5_sync_copy.loc[3,'Pushing{}'.format(b_li1[x])].replace(minute=50)
# #                 df5_sync.loc[df5_sync['hour']==hour, 'Pushing{}'.format(b_li1[x])]=df5_sync_copy['Pushing{}'.format(b_li1[x])].tolist()
# #             if n6==3:
# #
# #                 df6_sync_copy=df6_sync[df6_sync['hour']==hour].reset_index(drop=True)
# #                 df6_sync_copy.loc[0,'Pushing{}'.format(b_li2[x])]=df6_sync_copy.loc[0,'Pushing{}'.format(b_li2[x])].replace(minute=15)
# #                 df6_sync_copy.loc[1,'Pushing{}'.format(b_li2[x])]=df6_sync_copy.loc[1,'Pushing{}'.format(b_li2[x])].replace(minute=35)
# #                 df6_sync_copy.loc[2,'Pushing{}'.format(b_li2[x])]=df6_sync_copy.loc[2,'Pushing{}'.format(b_li2[x])].replace(minute=55)
# #                 df6_sync.loc[df6_sync['hour']==hour, 'Pushing{}'.format(b_li2[x])]=df6_sync_copy['Pushing{}'.format(b_li2[x])].tolist()
# #
# #             elif n6==4:
# #                 df6_sync_copy=df6_sync[df6_sync['hour']==hour].reset_index(drop=True)
# #                 df6_sync_copy.loc[0,'Pushing{}'.format(b_li2[x])]=df6_sync_copy.loc[0,'Pushing{}'.format(b_li2[x])].replace(minute=10)
# #                 df6_sync_copy.loc[1,'Pushing{}'.format(b_li2[x])]=df6_sync_copy.loc[1,'Pushing{}'.format(b_li2[x])].replace(minute=25)
# #                 df6_sync_copy.loc[2,'Pushing{}'.format(b_li2[x])]=df6_sync_copy.loc[2,'Pushing{}'.format(b_li2[x])].replace(minute=40)
# #                 df6_sync_copy.loc[3,'Pushing{}'.format(b_li2[x])]=df6_sync_copy.loc[3,'Pushing{}'.format(b_li2[x])].replace(minute=55)
# #                 df6_sync.loc[df6_sync['hour']==hour, 'Pushing{}'.format(b_li2[x])]=df6_sync_copy['Pushing{}'.format(b_li2[x])].tolist()
# #
# #
# #     df1.loc[df1['Oven No.{}'.format(b_li1[x])]!=' ','Pushing{}'.format(b_li1[x])]=df5_sync['Pushing{}'.format(b_li1[x])]
# #     df1.loc[df1['Oven No.{}'.format(b_li2[x])]!=' ','Pushing{}'.format(b_li2[x])]=df6_sync['Pushing{}'.format(b_li2[x])]
# #
# #     df1['Final5']=df1['Pushing{}'.format(b_li1[x])].apply(lambda x: x.strftime('%H:%M') if x!=' ' else x)
# #     df1['Final6']=df1['Pushing{}'.format(b_li2[x])].apply(lambda x: x.strftime('%H:%M') if x!=' ' else x)
# #
# #     df_li[x]=df1

# app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
#
# navbar = dbc.NavbarSimple(
#     children=[
#         dbc.Button("Sidebar", outline=True, color="secondary", className="mr-1", id="btn_sidebar"),
#         dbc.NavItem(dbc.NavLink("Page 1", href="#")),
#         dbc.DropdownMenu(
#             children=[
#                 dbc.DropdownMenuItem("More pages", header=True),
#                 dbc.DropdownMenuItem("Page 2", href="#"),
#                 dbc.DropdownMenuItem("Page 3", href="#"),
#             ],
#             nav=True,
#             in_navbar=True,
#             label="More",
#         ),
#     ],
#     brand="Brand",
#     brand_href="#",
#     color="dark",
#     dark=True,
#     fluid=True,
# )
#
#
# # the style arguments for the sidebar. We use position:fixed and a fixed width
# SIDEBAR_STYLE = {
#     "position": "fixed",
#     "top": 62.5,
#     "left": 0,
#     "bottom": 0,
#     "width": "16rem",
#     "height": "100%",
#     "z-index": 1,
#     "overflow-x": "hidden",
#     "transition": "all 0.5s",
#     "padding": "0.5rem 1rem",
#     "background-color": "#f8f9fa",
# }
#
# SIDEBAR_HIDEN = {
#     "position": "fixed",
#     "top": 62.5,
#     "left": "-16rem",
#     "bottom": 0,
#     "width": "16rem",
#     "height": "100%",
#     "z-index": 1,
#     "overflow-x": "hidden",
#     "transition": "all 0.5s",
#     "padding": "0rem 0rem",
#     "background-color": "#f8f9fa",
# }
#
# # the styles for the main content position it to the right of the sidebar and
# # add some padding.
# CONTENT_STYLE = {
#     "transition": "margin-left .5s",
#     "margin-left": "18rem",
#     "margin-right": "2rem",
#     "padding": "2rem 1rem",
#     "background-color": "#f8f9fa",
# }
#
# CONTENT_STYLE1 = {
#     "transition": "margin-left .5s",
#     "margin-left": "2rem",
#     "margin-right": "2rem",
#     "padding": "2rem 1rem",
#     "background-color": "#f8f9fa",
# }
#
# sidebar = html.Div(
#     [
#         html.H2("Sidebar", className="display-4"),
#         html.Hr(),
#         html.P(
#             "A simple sidebar layout with navigation links", className="lead"
#         ),
#         dbc.Nav(
#             [
#                 dbc.NavLink("Page 1", href="/page-1", id="page-1-link"),
#                 dbc.NavLink("Page 2", href="/page-2", id="page-2-link"),
#                 dbc.NavLink("Page 3", href="/page-3", id="page-3-link"),
#             ],
#             vertical=True,
#             pills=True,
#         ),
#     ],
#     id="sidebar",
#     style=SIDEBAR_STYLE,
# )
#
# content = html.Div(
#
#     id="page-content",
#     style=CONTENT_STYLE)
#
# app.layout = html.Div(
#     [
#         dcc.Store(id='side_click'),
#         dcc.Location(id="url"),
#         navbar,
#         sidebar,
#         content,
#     ],
# )
#
#
# @app.callback(
#     [
#         Output("sidebar", "style"),
#         Output("page-content", "style"),
#         Output("side_click", "data"),
#     ],
#
#     [Input("btn_sidebar", "n_clicks")],
#     [
#         State("side_click", "data"),
#     ]
# )
# def toggle_sidebar(n, nclick):
#     if n:
#         if nclick == "SHOW":
#             sidebar_style = SIDEBAR_HIDEN
#             content_style = CONTENT_STYLE1
#             cur_nclick = "HIDDEN"
#         else:
#             sidebar_style = SIDEBAR_STYLE
#             content_style = CONTENT_STYLE
#             cur_nclick = "SHOW"
#     else:
#         sidebar_style = SIDEBAR_STYLE
#         content_style = CONTENT_STYLE
#         cur_nclick = 'SHOW'
#
#     return sidebar_style, content_style, cur_nclick
#
# # this callback uses the current pathname to set the active state of the
# # corresponding nav link to true, allowing users to tell see page they are on
# @app.callback(
#     [Output(f"page-{i}-link", "active") for i in range(1, 4)],
#     [Input("url", "pathname")],
# )
# def toggle_active_links(pathname):
#     if pathname == "/":
#         # Treat page 1 as the homepage / index
#         return True, False, False
#     return [pathname == f"/page-{i}" for i in range(1, 4)]
#
#
# @app.callback(Output("page-content", "children"), [Input("url", "pathname")])
# def render_page_content(pathname):
#     if pathname in ["/", "/page-1"]:
#         return html.P("This is the content of page 1!")
#     elif pathname == "/page-2":
#         return html.P("This is the content of page 2. Yay!")
#     elif pathname == "/page-3":
#         return html.P("Oh cool, this is page 3!")
#     # If the user tries to reach a different page, return a 404 message
#     return dbc.Jumbotron(
#         [
#             html.H1("404: Not found", className="text-danger"),
#             html.Hr(),
#             html.P(f"The pathname {pathname} was not recognised..."),
#         ]
#     )
#
#
# if __name__ == "__main__":
#     app.run_server(debug=True, port=8086)
#





# import os
# import pathlib
# import pandas as pd
# from datetime import date
# from datetime import datetime as dt
# import numpy as np
# import pathlib
# import os
# import shutil
# from datetime import timedelta
# from tqdm import tqdm
# import plotly.graph_objs as go
# import plotly.offline as pyo
# import numpy as np
# from scipy import stats
# import plotly.express as px
#
# df_1=pd.read_csv('./datasets/CSV/TE Data/DM Data.csv',header=2,parse_dates=['Month'])
# df_1.dropna(thresh=10,inplace=True,axis=1)
# for c in df_1.columns:
#     if c!='Month':
#         df_1[c].replace(['-',' -','#DIV/0!'],0,inplace=True)
#         df_1[c]=df_1[c].astype(float)
#         df_1[c]=df_1[c].apply(lambda x: round(x,1))
#
# print(df_1.info())
# # df.columns=df.loc[1]
# # df.drop([0,1],inplace=True)
# # df_1=df.tail(15)
# # data=go.Scatter(
# #     x=df_1['Month'],
# #     y=df_1['CDQ POWER GEN'],
# #     mode='lines',
# #     fill='tozeroy',
# #     line={'shape': 'spline', 'smoothing': 1}
# # )
# # fig=go.Figure(data=data)
# # pyo.plot(fig)
# # print(df_1['CDQ POWER GEN'])
# # def range_dev(x):
# #     if x<-40:
# #         return 'less than -40'
# #     elif (x==-40)|(x==-30):
# #         return '-30 or -40'
# #     elif (x==30)|(x==40):
# #         return '30 or 40'
# #     elif x>40:
# #         return 'greater than 40'
# # df_c=pd.read_csv('./datasets/CSV/Battery5/PS Dev.csv')
# # df_c['date']=df_c['date'].apply(lambda x: dt.strptime(x,'%Y-%m-%d'))
# # df_c['dev']=df_c['dev'].apply(lambda x: int(x))
# # a=df_c[df_c['dev'].between(-20,20)].index.tolist()
# # df_c.drop(a,inplace=True)
# # #Getting x as dates & y as oven number
# # # df_c['date']=df_c['date'].apply(lambda x:dt.strptime(x,'%Y-%m-%d')) #Parsing dates
# # # a=df_c[df_c['oven']=='avg'].index
# # # df_c.drop(a,inplace=True)
# # ovens=df_c['oven'].unique().astype(str)
# # ovens=np.sort(ovens)
# # df_c=df_c[df_c['date'].between((dt.today()-timedelta(days=6)),dt.today())]
# # df_c['date']=df_c['date'].apply(lambda x:dt.date(x))
# #
# # df_c['dev_range']=df_c['dev'].apply(lambda x:range_dev(x))
# # df_c['dev_color']=df_c['dev'].apply(lambda x:abs(x))
# # df_c['dev_color']=df_c['dev_color'].apply(lambda x:str(x))
# # df_c=df_c.sort_values(['oven'])
# # df_c['oven']=df_c['oven'].apply(lambda x:str(x))
# # # df_c['dev']=df_c['dev'].apply(lambda x:str(x))
# # dates=df_c['date'].unique()
# # dates=np.sort(dates)
# # #Getting the z axis for heatmap(temperature)
# # temp=[[] for i in dates]
# # k=0
# # for i in dates:
# #     df_c_new=df_c[df_c['date']==i]
# #     for j in ovens:
# #         df_c_new_1=df_c_new[df_c_new['oven']==int(j)]
# #         if not(df_c_new_1.empty):
# #             temp[k].append(df_c_new_1['dev'].values.astype(int)[0])
# #         # else:
# #         #     temp[k].append(0)
# #     k+=1
# # #Defining graph attributes
# # fig=px.scatter(df_c,x='oven',y='date',color='dev',hover_data=['dev'],height=300,text='dev')
# # fig.update_layout(
# # plot_bgcolor='#FFF',
# # xaxis=dict(title='Deviations', linecolor='#808080', showgrid=False),
# # yaxis=dict(visible=True),
# # )
# # fig.update_traces(marker=dict(size=27),marker_symbol='square',textfont=dict(color='#F72119'))
# # data_c=[]
# # # for i in ovens:
# # #     for j in dates:
# # #         trace=go.Scatter(
# # #                 x=[i],
# # #                 y=[j],
# # #                 mode='markers'
# # #         )
# # #         data_c.append(trace)
# # layout=go.Layout(
# #     xaxis={'title':'Oven No.'},
# #     yaxis={'title':'VFs'},
# # )
# # pyo.plot(fig)
#
# # df=pd.read_csv(r'.\datasets\CSV\Battery7\CWT.csv', parse_dates=['date'])
# # df_new=df.loc[df['date'].between(dt(2021,7,1),dt(2021,7,31))]
# # df_new.drop(df_new[(df_new['oven']==701)|(df_new['oven']==781)].index.values.tolist(),inplace=True)
# # df_new.drop(df_new[(df_new['VFs']==1)|(df_new['VFs']==2)|(df_new['VFs']==27)|(df_new['VFs']==28)].index.values.tolist(),inplace=True)
# #
# # # index=df_new[((df_new['oven']==701)&(df_new['VFs']==1)|(df_new['VFs']==2)|(df_new['VFs']==27)|(df_new['VFs']==28))|((df_new['oven']==781)&(df_new['VFs']==1)|(df_new['VFs']==2)|(df_new['VFs']==27)|(df_new['VFs']==28))].index.values.tolist()
# # # index_oven=df_new[].index.values.tolist()
# # # df_new.drop(index,inplace=True)
# # # df_new.drop(index_oven,inplace=True)
# # df_new=df_new.sort_values('date')
# # df_new['Temp']=df_new['Temp'].astype(float).astype(int)
# # pusher=[]
# # for i in range(12):
# #     df_pusher=df_new[df_new['VFs']==(i+3)]
# #     pusher.append(df_pusher)
# # df_pusher_all=pd.concat(pusher)
# #
# # coke=[]
# # for i in range(12):
# #     df_coke=df_new[df_new['VFs']==(i+15)]
# #     coke.append(df_coke)
# # df_coke_all=pd.concat(coke)
# # ovens=df_pusher_all['oven'].unique()
# # avg=[]
# # for i in ovens:
# #     df_new=df[df['oven']==i]
# #     avg.append(df_new['Temp'].mean())
# #
#
#
# #
# # print('mean',np.mean(df_new['Temp']))
# # print('var',np.var(df_new['Temp']))
# # print('std',np.std(df_new['Temp']))
# # print('quartile',np.quantile(df_new['Temp'],[0.25,0.5,0.75]))
# # print('iqr',stats.iqr(df_new['Temp']))
# # print('max',np.max(df_new['Temp']))
# # print('min',np.min(df_new['Temp']))
# # print()
# # print('mean',np.mean(df_pusher_all['Temp']))
# # print('var',np.var(df_pusher_all['Temp']))
# # print('std',np.std(df_pusher_all['Temp']))
# # print('quartile',np.quantile(df_pusher_all['Temp'],[0.25,0.5,0.75]))
# # print('iqr',stats.iqr(df_pusher_all['Temp']))
# # print('max',np.max(df_pusher_all['Temp']))
# # print('min',np.min(df_pusher_all['Temp']))
# # print()
# # print('mean',np.mean(df_coke_all['Temp']))
# # print('var',np.var(df_coke_all['Temp']))
# # print('std',np.std(df_coke_all['Temp']))
# # print('quartile',np.quantile(df_coke_all['Temp'],[0.25,0.5,0.75]))
# # print('iqr',stats.iqr(df_coke_all['Temp']))
# # print('max',np.max(df_coke_all['Temp']))
# # print('min',np.min(df_coke_all['Temp']))
#
# # #
# # df=pd.read_csv(r'.\datasets\CSV\Battery7\controlps.csv', parse_dates=['date'])
# # df=df.loc[df['date'].between(dt(2021,7,1),dt(2021,7,31))]
# # df.drop(df[df['oven']=='avg'].index,inplace=True)
# # ovens_c=df_pusher_all['oven'].unique()
# # avg_c=[]
# # for i in ovens_c:
# #     df_new=df[df['oven']==str(i)]
# #     avg_c.append(df_new['temp'].mean())
# # trace1=go.Scatter(
# #     x=ovens,
# #     y=avg
# #     ,mode='lines'
# # )
# #
# #
# # trace2=go.Scatter(
# #     x=ovens_c,
# #     y=avg_c
# #     ,mode='lines'
# # )
# # fig=go.Figure(data=[trace1,trace2])
# # df_pusher_all['Temp'].reset_index(inplace=True,drop=True)
# # df['temp'].reset_index(inplace=True,drop=True)
# # # df_combine=pd.merge(df_pusher_all['Temp'],df['temp'])
# # diff=np.array(avg)-np.array(avg_c)
# # trace11=go.Scatter(
# #     x=ovens,
# #     y=diff
# #     ,mode='markers'
# # )
# # fig=go.Figure(data=[trace11])
# #
# # pyo.plot(fig)
# # print(df['temp'].mean())
# # print(df['temp'].std())
# # print(df['temp'].max())
# # print(df['temp'].min())
#

# df=pd.read_excel('./datasets/CSV/TE Data/DM Data.xlsx',engine='openpyxl')

# df.dropna(thresh=10,axis=1,inplace=True)
# df.columns=df.loc[1]
# df.drop([0,1],inplace=True)
# df=df.tail(31)
# print(df)
# df['3 MP']=df['3 MP'].astype(float)
# df['3 Prod Actual']=df['3 Prod Actual'].astype(float)
# df=df[['Month','4 MP','4 Prod Actual']].reset_index(drop=True)
# planned=[]
# actual=[]
# for i in range(df.shape[0]):
#     df_new=df.iloc[0:i,1:3]
#     planned.append(round(df_new.sum()[0],2))
#     actual.append(round(df_new.sum()[1],2))


# data5=go.Scatter(
#     x=df['Month'],
#     y=planned,
#      mode='lines',
#      line={'shape': 'spline', 'smoothing': 1}
# )
# data6=go.Scatter(
#     x=df['Month'],
#     y=actual,
#      mode='lines',
#      line={'shape': 'spline', 'smoothing': 1}
# )
# fig4=go.Figure(data=[data5,data6],layout=go.Layout(plot_bgcolor='#3E2C41',paper_bgcolor='#3E2C41',font_color='white',
#                 margin={'t':0.3,'l':0,'r':0,'b':0},
#                 xaxis=dict(linecolor='#3E2C41', showgrid=False),
#                 yaxis=dict(linecolor='#3E2C41',showgrid=False),
#                 font=dict(size=15),
#                 showlegend=False))
# ##pyo.plot(fig4)
# #pio.show(fig4)
# pyo.plot(fig4)
# #
# df=pd.read_excel('./datasets/CSV/TE Data/DM Data.xlsx',engine='openpyxl',header=[1,2])
# df.dropna(thresh=20,inplace=True,axis=1)
# for c in df.columns:
#     if c!=df.columns.values[0]:
#         df[c].replace(['-',' -'],0,inplace=True)
#         df[c]=df[c].astype(float)
#         df[c]=df[c].apply(lambda x: round(x,2))
# df_csr=df.loc[:,[df.columns.values[0],('CSR','3 CSR'),('CSR','4 CSR')]]
# df_csr.columns=['Date','3_CSR','4_CSR']
# df_csr=df_csr.tail(30)
# yr=(dt.today()-timedelta(days=400)).year
# year_2020=[]
# for index,rows in df_csr.iterrows():
#     year_2020.append(df_csr.iloc[index,0].year==2020)
# df_csr_prev_yr=df_csr.loc[year_2020]
# csr_3_std=round(df_csr_prev_yr['3_CSR'].std(),2)
# csr_4_std=round(df_csr_prev_yr['4_CSR'].std(),2)
# csr_3_mean=round(df_csr_prev_yr['3_CSR'].mean(),2)
# csr_4_mean=round(df_csr_prev_yr['4_CSR'].mean(),2)
# data1=go.Scatter(
#     x=df_csr['Date'],
#     y=df_csr['3_CSR'],
#     name='CSR 3',
#     # line={'shape': 'spline', 'smoothing': 1}
# )
# data2=go.Scatter(
#     x=df_csr['Date'],
#     y=df_csr['4_CSR'],
#     name='CSR 4',
#     line={'shape': 'spline', 'smoothing': 1}
# )
# fig=go.Figure(data=[data1,data2])
# fig.add_shape(type="line",
#     xref='paper',yref='y',
#     x0=0, y0=66, x1=1.0, y1=66,
#     # name='140 Amps line',
#     line=dict(
#     color="#778899",
#     width=2,
#     dash="longdashdot"
# ))
# df2.index=df2.Month
# df2.Month_yr=df2.Month.apply(lambda x: x.strftime('%b-%y'))
# #grouping by year
# df2 = df2.groupby(pd.Grouper(freq="M")).sum()
# df2.index=[x.strftime('%b-%y') for x in df2.index.tolist()]
# df2.Month_yr=df2.Month.apply(lambda x: x.strftime('%b-%y'))
# print(df_csr)
# # df=pd.read_excel(r'D:\Process KA Data\Battery5\5-Aug-21.xlsx',engine='openpyxl',sheet_name='SUMMARY', usecols=[i for i in range(34)])
# # Kb=df.loc[df[df['BAT']=='Kb'].index,'PUSHER SIDE'].values[0]
# # print(Kb)
# # df_p=pd.read_csv('./datasets/CSV/Battery5/PS DEV.csv', parse_dates=['date'])
# # df_p.drop(df_p[(df_p['oven']==501)|(df_p['oven']==581)].index.tolist(),inplace=True)
# # df_p=df_p[df_p['date']==dt(2021,8,16)]
# # df_p=df_p[(df_p.dev<=10)&(df_p.dev>=-10)]
# # pusher_side_ka_number=df_p.shape[0]
# #
# # df_c=pd.read_csv('./datasets/CSV/Battery5/CS DEV.csv', parse_dates=['date'])
# # df_c.drop(df_c[(df_c['oven']==501)|(df_c['oven']==581)].index.tolist(),inplace=True)
# # df_c=df_c[df_c['date']==dt(2021,8,16)]
# # df_c=df_c[(df_c.dev<=20)&(df_c.dev>=-20)]
# # coke_side_ka_number=df_c.shape[0]
# #
# # print(df_p)
# # ka=round((pusher_side_ka_number+coke_side_ka_number)/142,2)
# # print(ka,pusher_side_ka_number,coke_side_ka_number)
# #
# # planned_total_day=71
# # pcpd=(24*72)/float(planned_total_day)
# # #Parsing to timedelta for comparisons
# # pcpd=timedelta(seconds=(pcpd*60*60))
# # def parse_timedelta(s):
# #     days=s[1]
# #     s=s.split('T')[1]
# #     s=s.split('H')
# #     hours=s[0]
# #     s=s[1].split('M')
# #     mins=s[0]
# #     sec=s[1].split('S')[0]
# #     return timedelta(days=int(days),hours=int(hours), minutes=int(mins), seconds=int(sec))
# #
# # def dateswap(x):
# #     a=x.split('-')
# #     if len(a[0])==4:
# #         a[0],a[2]=a[2],a[0]
# #     return '{}-{}-{}'.format(a[0],a[1],a[2])
# #
# # dates=dt(2021,8,13)
# #
# # df1=pd.read_csv('./datasets/CSV/Battery5/Pushing-report.csv')
# # df1['Date']=df1['Date'].apply(lambda x: dateswap(x))
# # df1['Date']=df1['Date'].apply(lambda x: dt.strptime(x,'%d-%m-%Y'))
# # df1['ACPD']=df1['ACPD'].apply(lambda x:parse_timedelta(x))
# # df1['SCPD']=df1['SCPD'].apply(lambda x:parse_timedelta(x))
# # df1['Kcpd']=df1['ACPD'].apply(lambda x:1 if (x<(pcpd+timedelta(minutes=31)))&(x>(pcpd-timedelta(minutes=31))) else 0)
# # df1['Ku1']=df1['SCPD'].apply(lambda x:1 if (x<(pcpd+timedelta(minutes=31)))&(x>(pcpd-timedelta(minutes=31))) else 0)
# # df1['Ku2']=df1['SCPD'].apply(lambda x:1 if (x<(pcpd+timedelta(minutes=61)))&(x>(pcpd-timedelta(minutes=61))) else 0)
# # df=df1[df1['Date']==dates]
# # # print(df)
# # m,n=df.shape
# # Kcpd=round(df['Kcpd'].mean(),2)
# # Kp=round(df['Kp'].mean(),2)
# # Kc=round(df['Kc'].mean(),2)
# # '''------------max CPD-----------'''
# # df_CPD_max=df[df['ACPD']==df['ACPD'].max()]
# # max_CPD=df_CPD_max['Act. CPD'].values
# # oven_max_CPD=df_CPD_max['Oven No.'].values
# #
# # if oven_max_CPD.size==0:
# #     max_cpd_string=''
# # else:
# #     max_cpd_string='{}|{}'.format(int(oven_max_CPD[0]),max_CPD[0])
# #
# # '''------------min CPD-----------'''
# #
# # df_CPD_min=df[df['ACPD']==df['ACPD'].min()]
# # min_CPD=df_CPD_min['Act. CPD'].values
# # oven_min_CPD=df_CPD_min['Oven No.'].values
# # if oven_min_CPD.size==0:
# #     min_cpd_string=''
# # else:
# #     min_cpd_string='{}|{}'.format(int(oven_min_CPD[0]),min_CPD[0])
# # '''-------------max AMP----------------'''
# # df_amp_max=df[df['Amperage']==df['Amperage'].max()]
# # max_amp=df_amp_max['Amperage'].values
# # oven_max_amp=df_amp_max['Oven No.'].values
# # if oven_max_amp.size==0:
# #     max_amp_string=''
# # else:
# #     max_amp_string='{}|{}'.format(int(oven_max_amp[0]),max_amp[0])
# # '''-------------mean AMP----------------'''
# # df_amp_mean=round(df['Amperage'].mean(),2)
# # '''-------------mean CPD----------------'''
# # cpd_mean=df['ACPD'].mean(numeric_only=False)
# #
# # a0=df['Kp'].sum()
# # a30=df['a30'].sum()
# # a60=df['a60'].sum()
# # planned_total_day=int(planned_total_day)
# #
# # # Kcpd=round(df['Kcpd'].mean(),2)
# # # Kp=round(df['Kp'].mean(),2)
# # # Kc=round(df['Kc'].mean(),2)
# #
# # Ku1=round(df['Ku1'].sum()/73,3)
# # Ku2=round(df['Ku2'].mean(),3)
# # Kexe=round(a0/m,2)
# # Kgen1=round(Ku1*Kexe,2)
# # Kgen2=round(Ku2*Kexe,2)
# #
# # ku1_=round(df['Ku1'].sum()/71,3)
# # ku2_=round(df['Ku2'].sum()/71,3)
# # kexe__=round(a0/71,2)
# # kgen1_=round(Ku1*Kexe,2)
# # kgen2_=round(Ku2*Kexe,2)
# # kcpd_=round(df['Kcpd'].sum()/71,2)
# # kc_=round(df['Kc'].sum()/71,2)
# # kp_=round(df['Kp'].sum()/71,2)
# # print('pcpd',pcpd)
# # print('sum of kcpd',df['Kcpd'].sum())
# # print('Kcpd',Kcpd,kcpd_)
# # print('Kp',Kp,kp_)
# # print('Kc',Kc,kc_)
# # print('Ku1',Ku1,ku1_)
# # print('Ku2',Ku2,ku2_)
# # print('Kexe',Kexe,kexe__)
# # print('Kgen1',Kgen1,kgen1_)
# # print('Kgen2',Kgen2,kgen2_)
# # print(df[['ACPD','Kcpd']].to_csv('kcpd.csv'))
# # print(Ku1,Ku2,Kexe,Kgen1,Kgen2)
# # # df_day=pd.DataFrame(
# # # {
# # # 'Date':[date_string]*13,
# # # 'Shift':['Day']*13,
# # # 'K':['Kcpd','Kp','Kc','Ku1','Ku2','Kexe','Kgen1','Kgen2','Max. CPD','Min. CPD','Average CPD','Max. Amperage','Mean Amperage'],
# # # 'Value':[Kcpd,Kp,Kc,Ku1,Ku2,Kexe,Kgen1,Kgen2,max_cpd_string,min_cpd_string,cpd_mean,max_amp_string,df_amp_mean]
# # # }
# # # )
# # print(pcpd,Kcpd)
# # planned_total_day=70
# # pcpd=(24*72)/float(planned_total_day)
# # pcpd=timedelta(seconds=(pcpd*60*60))
#
#
# # df1=pd.read_csv('./datasets/CSV/Battery5/Pushing-report.csv')
# # df1['Date']=df1['Date'].apply(lambda x: dateswap(x))
# # df1['Date']=df1['Date'].apply(lambda x: dt.strptime(x,'%d-%m-%Y'))
# # df1['ACPD']=df1['ACPD'].apply(lambda x:parse_timedelta(x))
# # df1['SCPD']=df1['SCPD'].apply(lambda x:parse_timedelta(x))
# # df1['Kcpd']=df1['ACPD'].apply(lambda x:1 if (x<=(pcpd+timedelta(minutes=30)))&(x>=(pcpd-timedelta(minutes=30))) else 0)
# # df1['Ku1']=df1['SCPD'].apply(lambda x:1 if (x<=(pcpd+timedelta(minutes=30)))&(x>=(pcpd-timedelta(minutes=30))) else 0)
# # df1['Ku2']=df1['SCPD'].apply(lambda x:1 if (x<=(pcpd+timedelta(minutes=60)))&(x>=(pcpd-timedelta(minutes=60))) else 0)
#
#
# # '''-------------------------------dailydev----------------------------------'''
# #
# # df=pd.read_csv('./datasets/CSV/Battery5/CS DEV.csv', parse_dates=['date'])
# # df=df.groupby(['date','dev']).count().reset_index()
# # df.columns=['date','dev','count']
# # df=df[(df['dev']>=30)|(df['dev']<=-30)]
# # df['count']=df.apply(lambda row:row['count']*-1 if row['dev']<0 else row['count']*1,axis=1)
# # df['dev']=df.apply(lambda row:row['dev']*-1 if row['dev']<0 else row['dev']*1,axis=1)
# # df['date']=df['date'].apply(lambda x:dt.date(x))
# # df['text']=df['count'].apply(lambda x:x*-1 if x<0 else x)
# #
# # df=df[df['date']==c]
# #
# # data=go.Bar(
# # x=df['dev'].astype(str),
# # y=df['count'],
# # text=df['text'],
# # textposition='inside'
# # )
# # layout=go.Layout(
# # title='adsf',
# # yaxis=dict(visible=True)
# #
# # )
# #
# # fig=go.Figure(
# # data=data,layout=layout,
# # )
# # pyo.plot(fig)
# #
# # '''--------------------------------ovenwisedev-------------------------------'''
# # # df_p=pd.read_csv('./datasets/CSV/Battery5/PS Actions.csv', parse_dates=['date'])
# # # df_c=pd.read_csv('./datasets/CSV/Battery5/CS Actions.csv', parse_dates=['date'])
# # # #filtering pusher side data
# # # df_p=df_p[df_p['oven']==501]
# # # df_p=df_p.tail(3)   #last three entries
# # # df_p['date']=df_p['date'].apply(lambda x:dt.date(x).strftime('%d-%B-%y'))   #Converting datetime to date
# # # #filtering coke side data
# # # df_c=df_c[df_c['oven']==501]
# # # df_c=df_c.tail(3)   #last three entries
# # # df_c['date']=df_c['date'].apply(lambda x:dt.date(x).strftime('%d-%B-%y'))
# # df=pd.read_csv('./datasets/CSV/Battery5/Pushing-report.csv',parse_dates=['Date'])
# # df=df[df['Date']==dt(2021,7,26,0,0,0)]
# # print(df.to_csv('psuhifnasb.csv'))
# # print(df_c)
# # df['date']=df['date'].apply(lambda x:dt.date(x))
# # c=dt.strptime('2021-7-15','%Y-%m-%d')
# # c=dt.date(c)
# # df=df[df['date']==c]                                #Date
# # df=df[(df['dev']==30)|(df['dev']==-30)]             #Type of deviation
# #
# #
# # data=go.Scatter(
# # x=df['oven'].astype(str),
# # y=df['dev'],
# # mode='markers'
# # )
# #
# # layout=go.Layout(
# # title='dasads'
# # )
# #
# # fig=go.Figure(
# # data=data,layout=layout
# # )
# #
# # pyo.plot(fig)
