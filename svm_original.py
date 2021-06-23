from sklearn.metrics import classification_report, confusion_matrix, f1_score, roc_auc_score, accuracy_score
from sklearn import svm
from sklearn.svm import LinearSVC

def train_svm( train_sample_data, train_sample_label, test_data, test_label, validation_data, validation_label):

    # Train for different values of c and find the best using a validation.
    roc_values = []
    c_values = [.1, 1, 10, 100]


    for c_value in c_values:

        # Fit a linear classifier
        svclassifier = svm.SVC(kernel='linear', C= c_value)
        svclassifier.fit(train_sample_data, train_sample_label)

        # Take the validation input
        y_pred = svclassifier.predict(validation_data)
        roc = roc_auc_score(validation_label,y_pred)
        roc_values.append ( roc )

    c = c_values[roc_values.index( max(roc_values) )]

    svclassifier = svm.SVC(kernel='linear', C=c)
    svclassifier.fit(train_sample_data, train_sample_label)

    y = svclassifier.predict(test_data)
    roc_test = roc_auc_score(test_label, y)
    f1 = f1_score(test_label, y)
    accuracy = accuracy_score(test_label, y)

    return accuracy, roc_test
