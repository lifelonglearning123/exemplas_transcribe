import streamlit as st
import pandas as pd







def main():
    st.title('Exemplas Transcribe & Summarisation App')
    st.write("Please upload audio file.")

    uploaded_master_file = st.file_uploader("Audio File", key="master", type=['mp3'])
    uploaded_check_file = st.file_uploader("Transcribe Text", key="check", type=['xlsx'])

    if uploaded_master_file and uploaded_check_file:
        master = pd.read_excel(uploaded_master_file, sheet_name=0)
        check = pd.read_excel(uploaded_check_file, sheet_name=0)

        updated_check = update_check_file_with_master_data(master, check)
        updated_check = update_check_file_with_master_reg(master, updated_check)

        updated_check['Company Registration Number'] = updated_check['Company Registration Number'].fillna('').astype(str)
        updated_check['Reg Compare'] = updated_check['Reg Compare'].fillna('').astype(str)
        updated_check['Updated Column B'] = updated_check['Updated Column B'].fillna('').astype(str)

        updated_check = update_check_with_combined_status(updated_check)

        st.write("Check file after updating with data from the master file:")
        st.dataframe(updated_check)

if __name__ == "__main__":
    main()
