bool checkBSTHelper(Node* root, int min, int max){
	if(root == NULL)
		return true;
	if(root->data <= min || root->data >= max)
		return false;
        return checkBSTHelper(root->left, min, root->data) && checkBSTHelper(root->right, root->data, max);
}

bool checkBST(Node* root) {
	return checkBSTHelper(root,INT_MIN,INT_MAX);
}