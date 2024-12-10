from shipment.pipeline.training_pipeline import TrainPipeline

if __name__ == "__main__":
    try:
        pipeline = TrainPipeline()
        pipeline.run_pipeline()
        print("Pipeline executed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
