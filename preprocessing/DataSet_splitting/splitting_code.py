import pandas as pd



# DATASET SCHEMAS

DATASET_COLUMNS = {

    "FIR": {

        "NOT_GT": [
            "fir_number",
            "case_id",
            "event_id",
            "evidence_id",
            "evidence_group_id",
            "source_record_id",
            "police_station",
            "district",
            "registration_date",
            "registration_time",
            "incident_date",
            "incident_time",
            "offence_category",
            "complainant_id",
            "persons_mentioned",
            "incident_location",
            "location_id",
            "vehicle_number",
            "complainant_contact",
            "contact_numbers",
            "person_1_contact",
            "person_2_contact",
            "person_3_contact",
            "narrative",
            "evidence_mentioned",
            "source_reliability"
        ],

        "GT": [
            "case_status",
            "case_outcome",
            "case_difficulty",
            "relationship_truth",
            "evidence_role",
            "evidence_strength",
            "ground_truth_split",
            "dataset_split",
            "case_network_type",
            "person_ground_truth_summary"
        ]
    },


    "Communications": {

        "NOT_GT": [
            "communication_id",
            "sender_id",
            "receiver_id",
            "sender_contact",
            "receiver_contact",
            "source",
            "timestamp",
            "latitude",
            "longitude",
            "location",
            "location_id",
            "device_id",
            "message",
            "communication_type",
            "case_id",
            "event_id",
            "evidence_id",
            "evidence_group_id",
            "source_record_id",
            "source_reliability"
        ],

        "GT": [
            "relationship_strength",
            "relationship_truth",
            "evidence_role",
            "evidence_strength",
            "data_quality_flag",
            "anomaly_type",
            "dataset_split",
            "ground_truth_available_for_evaluation",
            "case_network_type",
            "relationship_active",
            "relationship_start_date",
            "relationship_end_date"
        ]
    },


    "CDR": {

        "NOT_GT": [
            "cdr_id",
            "caller_id",
            "caller_number",
            "receiver_id",
            "receiver_number",
            "call_date",
            "call_time",
            "call_type",
            "duration_seconds",
            "cell_tower_id",
            "cell_tower_name",
            "latitude",
            "longitude",
            "location_id",
            "imei",
            "sim_id",
            "call_status",
            "case_id",
            "event_id",
            "evidence_id",
            "evidence_group_id",
            "source_record_id",
            "source_reliability"
        ],

        "GT": [
            "relationship_strength",
            "relationship_truth",
            "evidence_role",
            "evidence_strength",
            "data_quality_flag",
            "anomaly_type",
            "dataset_split",
            "ground_truth_available_for_evaluation",
            "case_network_type",
            "relationship_active",
            "relationship_start_date",
            "relationship_end_date"
        ]
    },


    "Financial": {

        "NOT_GT": [
            "transaction_id",
            "person_id",
            "contact_number",
            "account_number",
            "counterparty_person_id",
            "counterparty_account",
            "counterparty_contact",
            "transaction_date",
            "transaction_time",
            "transaction_type",
            "direction",
            "amount",
            "currency",
            "bank",
            "merchant_or_recipient",
            "transaction_status",
            "purpose",
            "location",
            "location_id",
            "case_id",
            "event_id",
            "evidence_id",
            "evidence_group_id",
            "source_record_id",
            "relationship_type",
            "source_reliability"
        ],

        "GT": [
            "relationship_strength",
            "relationship_truth",
            "evidence_role",
            "evidence_strength",
            "anomaly_type",
            "data_quality_flag",
            "dataset_split",
            "ground_truth_available_for_evaluation",
            "case_network_type",
            "relationship_active",
            "relationship_start_date",
            "relationship_end_date"
        ]
    },


    "Locations": {

        "NOT_GT": [
            "location_id",
            "person_id",
            "contact_number",
            "device_id",
            "date",
            "time",
            "latitude",
            "longitude",
            "location",
            "location_type",
            "confidence",
            "case_id",
            "event_id",
            "evidence_id",
            "evidence_group_id",
            "source_record_id",
            "source_reliability"
        ],

        "GT": [
            "evidence_role",
            "evidence_strength",
            "data_quality_flag",
            "anomaly_type",
            "dataset_split",
            "ground_truth_available_for_evaluation",
            "case_network_type",
            "relationship_active",
            "relationship_start_date",
            "relationship_end_date"
        ]
    }
}


# ============================================================
# DETECT DATASET TYPE
# ============================================================

def detect_dataset_type(df):

    df_columns = set(df.columns)

    matches = {}

    for dataset_name, column_groups in DATASET_COLUMNS.items():

        expected_columns = (
            set(column_groups["NOT_GT"])
            | set(column_groups["GT"])
        )

        matched_columns = df_columns.intersection(expected_columns)

        match_percentage = (
            len(matched_columns) / len(expected_columns)
        )

        matches[dataset_name] = match_percentage

    detected_dataset = max(matches, key=matches.get)
    best_match = matches[detected_dataset]

    if best_match < 0.90:
        print("\nDataset detection failed.")
        print("\nSchema match results:")

        for dataset_name, score in matches.items():
            print(f"{dataset_name}: {score:.2%}")

        raise ValueError(
            "Could not reliably identify the dataset type."
        )

    return detected_dataset, best_match


# SPLIT GT AND NOT-GT COLUMNS

def split_gt_columns(df):

    # Validate input


    if not isinstance(df, pd.DataFrame):
        raise TypeError(
            "df must be a pandas DataFrame."
        )

    if df.empty:
        raise ValueError(
            "The DataFrame is empty."
        )


    # Detect dataset


    dataset_type, match_percentage = detect_dataset_type(df)

    print("\nDataset detected:", dataset_type)
    print("Schema match:", f"{match_percentage:.2%}")

        # Get GT and NOT-GT columns
    
    not_gt_columns = DATASET_COLUMNS[dataset_type]["NOT_GT"]
    gt_columns = DATASET_COLUMNS[dataset_type]["GT"]


    # Check for missing columns
    
    missing_not_gt = [
        column
        for column in not_gt_columns
        if column not in df.columns
    ]

    missing_gt = [
        column
        for column in gt_columns
        if column not in df.columns
    ]

    if missing_not_gt:
        print("\nWARNING - Missing NOT-GT columns:")
        print(missing_not_gt)

    if missing_gt:
        print("\nWARNING - Missing GT columns:")
        print(missing_gt)

    
    # Keep only columns that actually exist
    

    not_gt_columns = [
        column
        for column in not_gt_columns
        if column in df.columns
    ]

    gt_columns = [
        column
        for column in gt_columns
        if column in df.columns
    ]


    # Create two DataFrames


    df_train = df[not_gt_columns].copy()

    df_evaluate = df[gt_columns].copy()


    # File names


    train_filename = f"df_{dataset_type}_train.csv"

    evaluate_filename = f"df_{dataset_type}_evaluate.csv"

    
    # Save CSV files
    

    df_train.to_csv(
        train_filename,
        index=False
    )

    df_evaluate.to_csv(
        evaluate_filename,
        index=False
    )

    
    # Display summary
    

    print("\n" + "=" * 60)
    print("DATASET SPLIT COMPLETED")
    print("=" * 60)

    print(f"Dataset detected : {dataset_type}")
    print(f"Schema match     : {match_percentage:.2%}")

    print("\nOriginal dataset:")
    print(f"Rows    : {len(df)}")
    print(f"Columns : {len(df.columns)}")

    print("\nNOT-GT dataset:")
    print(f"Rows    : {len(df_train)}")
    print(f"Columns : {len(df_train.columns)}")
    print(f"Saved as: {train_filename}")

    print("\nGT dataset:")
    print(f"Rows    : {len(df_evaluate)}")
    print(f"Columns : {len(df_evaluate.columns)}")
    print(f"Saved as: {evaluate_filename}")

    return df_train, df_evaluate



# MAIN PROGRAM


if __name__ == "__main__":

    # Change this to your CSV filename/path
    input_file = "synthetic_criminal_network_locations.csv"

    # Load dataset
    df = pd.read_csv(input_file)

    # View information
    print(df.info())

    # Split into NOT-GT and GT
    df_train, df_evaluate = split_gt_columns(df)