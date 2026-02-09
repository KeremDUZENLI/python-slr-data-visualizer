import os
import streamlit as st

from config.maps import COUNTRY_TO_CONTINENT
from input._1_read import read_dataset
from input._2_prepare import (
    group_dataset_by_fields,
    map_dataset_column,
)


st.set_page_config(layout="wide", page_title="SLR Data Visualizer")
st.title("SLR Data Visualization Tool")

uploaded_file = st.file_uploader("Upload Dataset (CSV)", type="csv")
if uploaded_file:
    ### read_dataset ###
    temp_path = "temp_dataset.csv"
    with open(temp_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    DATASET = read_dataset(csv_path=temp_path)
    os.remove(temp_path)

    ### group_dataset_by_fields ###
    st.sidebar.header("Group Dataset by Fields")

    field_name_new = st.sidebar.text_input("Field Name New (software)")
    category_name = st.sidebar.text_input("Category Name (software_category)")
    fields_all = list(DATASET.keys())

    fields_to_combine = st.sidebar.multiselect(
        "Fields to combine into " + field_name_new,
        options=fields_all,
    )
    fields_other = st.sidebar.multiselect(
        "Fields Other (year, technique)",
        options=fields_all,
    )

    if st.sidebar.button("Group Dataset"):
        dataset_and_maps = []

        for field in fields_to_combine:
            mapping = {}
            mapping[field_name_new] = field

            for field_other in fields_other:
                mapping[field_other] = field_other

            dataset_and_maps.append((DATASET, mapping))

        axes = [category_name, field_name_new] + fields_other
        DATASET_STACKED = group_dataset_by_fields(
            datasets=dataset_and_maps,
            stack_by={category_name: field_name_new},
            axes=axes,
        )

        st.divider()
        st.subheader("✅ Group Dataset by Fields: {}".format(category_name))
        col1, col2 = st.columns(2)
        col1.metric("Rows in Original", len(DATASET[fields_all[0]]))
        col2.metric("Rows in Stacked", len(DATASET_STACKED[category_name]))

        st.dataframe(DATASET_STACKED, use_container_width=True)
